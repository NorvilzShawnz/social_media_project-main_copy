from django.http import HttpResponse
from json import dumps
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate

from .models import VibeGroup, VibeUser, VibePost, VibeComment
# Importing sample data for testing purposes
from . import sample_data
from .sample_data import SamplePosts

User = get_user_model()

authenticatedUser = VibeUser.objects.get(username='HikeHigh')

authenticatedUserPosts = VibePost.objects.filter(author=authenticatedUser)

usersToFollow = VibeUser.objects.filter(username__in=('HikeHigh', 'JAlderson', 'antoniollanes', 'sls0013', 'Adrian5234'))
usersToFollow = usersToFollow.exclude(id=authenticatedUser.id)

allGroupPosts = VibePost.objects.filter(id__in=(7, 8))

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('content'):
            new_post = VibePost.objects.create(
                author = authenticatedUser,
                contents = request.POST.get('content'),
                media = None,
                like_cnt = 0,
                share_cnt = 0,
                comment_cnt = 0,
            )
            new_post.save()
        # elif request.POST['comment_content']:
        #     comment_content = request.POST['comment_content']
        #     post_replied_to_id = request.POST['post_replied_to_id']
        #     post_replied_to = VibePost.objects.get(id=post_replied_to_id)
            
        #     new_comment = VibeComment.objects.create(
        #         post_replied_to = post_replied_to,
                
        #         author = authenticatedUser,
        #         contents = comment_content,
        #         media = None,
        #         like_cnt = 0,
        #         share_cnt = 0,
        #         comment_cnt = 0,
        #     )
        #     new_comment.save()
    
    if request.GET.get('post_to_like_id'):
        post_to_like_id = request.GET.get('post_to_like_id')
        post_to_like = VibePost.objects.get(id=post_to_like_id)
        post_to_like.like_cnt += 1
        post_to_like.save()
        
    if request.GET.get('post_shared_id'):
        post_shared_id = request.GET.get('post_shared_id')
        post_shared = VibePost.objects.get(id=post_shared_id)
        post_shared.share_cnt += 1
        post_shared.save()
        
    postsInFeed = VibePost.objects.difference(allGroupPosts).order_by('-date_time_posted') #difference(authenticatedUserPosts)
    context = {
        'authenticatedUser' : authenticatedUser,
        'postsInFeed' : postsInFeed,
        'usersToFollow' : usersToFollow
    }
        
    return render(request, "index.html", context)

def profile(request):
    
    
    profile_owner_id = int( request.GET.get("profile_owner_id") )
    
    profileOwner = VibeUser.objects.get(id=profile_owner_id)
    postsUserMade = VibePost.objects.filter(author=profileOwner).difference(allGroupPosts)
    context = {
        'authenticatedUser' : authenticatedUser,
        'profileOwner' : profileOwner,
        'postsUserMade' : postsUserMade,
        'usersToFollow' : usersToFollow
    }
    return render(request, "profile.html", context)

def settings(request):
    
    context = {
        'authenticatedUser' : authenticatedUser
    }
    return render(request, "settings.html", context)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('/')  # or wherever your landing page is
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('signin')

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        dob = request.POST.get('dob')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            date_of_birth=dob
        )
        user.save()

        #  Log the user in right after signup
        login(request, user)

        messages.success(request, f"Welcome, {user.username}!")
        return redirect('/')  # Change to whatever view you want to redirect to after login

    return render(request, 'signup.html')

def advanced_search(request):
    posts = VibePost.objects.all()

    if request.method == "POST":
        post_author = request.POST.get("post_author", "").strip()
        if post_author:
            posts = posts.filter(author__username__icontains=post_author)

        all_words = request.POST.get("all_of_these_words", "")
        any_words = request.POST.get("any_of_these_words", "")
        none_words = request.POST.get("none_of_these_words", "")

        if all_words:
            for word in all_words.split():
                posts = posts.filter(contents__icontains=word)
    
        if any_words:
            queries = Q()
            for word in any_words.split():
                queries |= Q(contents__icontains=word)
            posts = posts.filter(queries)

        if none_words:
            for word in none_words.split():
                posts = posts.exclude(contents__icontains=word)

        try:
            likes_lt = int(request.POST.get("likes_lt", 9999999999.9))
            posts = posts.filter(like_cnt__lt=likes_lt)
        except ValueError:
            pass

        try:
            likes_gt = int(request.POST.get("likes_gt", float(-9999999999.9)))
            posts = posts.filter(like_cnt__gt=likes_gt)
        except ValueError:
            pass

        try:
            replies_lt = int(request.POST.get("replies_lt", float(9999999999.9)))
            posts = posts.filter(comment_cnt__lt=replies_lt)
        except ValueError:
            pass

        try:
            replies_gt = int(request.POST.get("replies_gt", float(-9999999999.9)))
            posts = posts.filter(comment_cnt__gt=replies_gt)
        except ValueError:
            pass


        try:
            shares_lt = int(request.POST.get("shares_lt", float(9999999999.9)))
            posts = posts.filter(share_cnt__gt=shares_lt)
        except ValueError:
            pass

        try:
            shares_gt = int(request.POST.get("shares_gt", float(-9999999999.9)))
            posts = posts.filter(share_cnt__gt=shares_gt)
        except ValueError:
            pass

        date_before = request.POST.get("date_before")
        date_after = request.POST.get("date_after")

        if date_before:
            posts = posts.filter(date_time_posted__lt=date_before)

        if date_after:
            posts = posts.filter(date_time_posted__gt=date_after)
    
        was_edited = request.POST.get("was_edited")
        if was_edited == "Yes":
            posts = posts.filter(is_edited=True)
        elif was_edited == "No":
            posts = posts.filter(is_edited=False)

        has_media = request.POST.get("has-media")
        if has_media == "Yes":
            posts = posts.filter(media__isnull=False)
        elif has_media == "No":
            posts = posts.filter(media__isnull=True)


        sorting_1 = request.POST.get("sorting-1")
        sorting_order_1 = request.POST.get("sorting-order-1")
        sorting_2 = request.POST.get("sorting-2")
        sorting_order_2 = request.POST.get("sorting-order-2")

        if sorting_1 != "N/A":
            if sorting_order_1 == "Descending":
                posts = posts.order_by(f"-{sorting_1.lower()}")
            else:
                posts = posts.order_by(sorting_1.lower())

        if sorting_2 != "N/A":
            if sorting_order_2 == "Descending":
                posts = posts.order_by(f"-{sorting_2.lower()}")
            else:
                posts = posts.order_by(sorting_2.lower())

    context = {
        "postsInFeed": posts,
        "authenticatedUser": authenticatedUser,
    }

    return render(request, "advanced-search.html", context)

def view_post(request):
    # authenticatedUser = request.user
    
    if request.method == 'POST':
        viewed_post_id = request.POST.get("post_replied_to_id")
        
        comment_content = request.POST['comment_content']
        post_replied_to = VibePost.objects.get(id=viewed_post_id)
        
        new_comment = VibeComment.objects.create(
            post_replied_to = post_replied_to,
            
            author = authenticatedUser,
            contents = comment_content,
            media = None,
            like_cnt = 0,
            share_cnt = 0,
            comment_cnt = 0,
        )
        new_comment.save()
    else:
        viewed_post_id = request.GET.get("viewed_post_id")
    
    viewed_post_id = int(viewed_post_id)
    # Grab the post or 404
    post = get_object_or_404(VibePost, id=viewed_post_id)
    # Filter only comments for this post
    post_comments = VibeComment.objects.filter(post_replied_to=post).order_by('-date_time_posted')

    
    usersToFollow = VibeUser.objects.exclude(id=authenticatedUser.id)[:5]

    context = {
        'authenticatedUser': authenticatedUser,
        'listWithViewedPost': [post],
        'postComments': post_comments,
        'usersToFollow': usersToFollow
    }

    return render(request, "view-post.html", context)


def find_groups(request):
    groupsDisplayed = VibeGroup.objects.all()

    context = {
        'authenticatedUser' : authenticatedUser,
        'groupsDisplayed' : groupsDisplayed
    }
    return render(request, "find-groups.html", context)

def group_page(request):
    
    displayed_group_id = int( request.GET.get("displayed_group_id") )
    displayed_group = VibeGroup.objects.get(id=displayed_group_id)
    groupPosts = allGroupPosts
    
    context = {
        'authenticatedUser' : authenticatedUser,
        'group' : displayed_group,
        'groupPosts' : groupPosts,
    }
    return render(request, "group-page.html", context)

def find_users(request):
    usersDisplayed = VibeUser.objects.all()
    context = {
        'authenticatedUser' : authenticatedUser,
        'usersDisplayed' : usersDisplayed
    }
    return render(request, "find-users.html", context)