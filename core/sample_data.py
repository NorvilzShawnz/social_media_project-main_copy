# This is dummy data used for testing purposes. The final project version should get data from the actual database.

from .models import VibeUser, VibeGroup, VibePost, VibeComment

# Schema for User:
# User = (id, displayname, username, password, profile_pic, banner_pic, bio, location, email, date_of_birth, follower_cnt, follows_cnt, post_cnt, is_verified, any other fields in the default user model)

SampleUsers = [
    { 
        'id': 0,
        'displayname': '#1 HIKING WORLD CHAMPION',
        'username': 'HikeHigh',
        'password': 'arewethereyet',
        'profile_pic': 'profile-images/Snow-mountain-graphic.png',
        'banner_pic': 'banners/Snow-mountains-banner.jpg',
        'bio': 'This is your bio. Edit it with descriptions about yourself.',
        'location': 'Tallahassee, FL',
        'email': "A@gmail.com",
        'date_of_birth': '2001-01-01',
        'follower_cnt': 1,
        'follows_cnt': 1,
        'post_cnt': 2,
        'is_verified': False,
    },
    { 
        'id': 1,
        'displayname': 'Adrian!!!',
        'username': 'Adrian5234',
        'password': 'abc123',
        'profile_pic': None,
        'banner_pic': None,
        'bio': '',
        'location': '',
        'email': "B@gmail.com",
        'date_of_birth': '2000-01-01',
        'follower_cnt': 2,
        'follows_cnt': 7,
        'post_cnt': 1,
        'is_verified': False,
    },
    { 
        'id': 2,
        'displayname': 'Can You Not',
        'username': 'sls0013',
        'password': 'abc123',
        'profile_pic': None,
        'banner_pic': None,
        'bio': '',
        'location': '',
        'email': "C@gmail.com",
        'date_of_birth': '2000-01-01',
        'follower_cnt': 15,
        'follows_cnt': 2,
        'post_cnt': 1,
        'is_verified': False,
    },
    { 
        'id': 3,
        'displayname': 'Joseph Alderson',
        'username': 'JAlderson',
        'password': 'arewethereyet',
        'profile_pic': 'profile-images/false-noise-scarlet-red.png',
        'banner_pic': 'banners/video-game-banner.png',
        'bio': 'Vibespace administrator and stressed out student studying computer science at FSU. DM me if you have any questions.',
        'location': 'Tallahassee, FL',
        'email': "D@gmail.com",
        'date_of_birth': '2000-01-01',
        'follower_cnt': 1285,
        'follows_cnt': 112,
        'post_cnt': 1,
        'is_verified': True,
    },
]
SampleUsersToFollow = [SampleUsers[1], SampleUsers[2], SampleUsers[3]]
SampleAuthenticatedUser = SampleUsers[0]

# Creating content for very long post, just for fun
andOnAndOn = ''
for i in range(50):
    andOnAndOn += " and on and on and on and on and on and on and on and on"

# Schema for Post (Just assume each post can only have 1 image as its media):
# Post = (id, author, contents, media, date_time_posted, like_cnt, share_cnt, comment_cnt)
SamplePosts = [ # DateTime fields are of the form '2006-10-25 14:30:59'
    {
        'id': 0,
        'author': SampleUsers[1],
        'contents' : 'Hello, I am a sample post.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 32274,
        'share_cnt': 34587,
        'comment_cnt': 6
    },
    {
        'id': 1,
        'author': SampleUsers[2],
        'contents' : 'I love the outdoors!',
        'media' : 'post-media/mountains.jpg',
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 3,
        'share_cnt': 3,
        'comment_cnt': 0
    },
    {
        'id': 2,
        'author': SampleUsers[0],
        'contents' : 'This is an example of something that the currently logged in user posted. On this page, only posts that that user posted can show up.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 3,
        'share_cnt': 3,
        'comment_cnt': 0
    },
    {
        'id': 3,
        'author': SampleUsers[0],
        'contents' : 'On Vibespace, posts have almost no character limit. This means posts can go on' + andOnAndOn,
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 3,
        'share_cnt': 3,
        'comment_cnt': 0
    },
    {
        'id': 4,
        'author': SampleUsers[3],
        'contents' : 'Been staying up past 6 am just trying to make this site the best it can be.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 1560,
        'share_cnt': 33,
        'comment_cnt': 0
    },
    {
        'id': 5,
        'author': SampleUsers[3],
        'contents' : 'The latest VibeSpace update now features like, share, and comment buttons. You can also view posts and their comments!',
        'media' : 'post-media/VibeSpace-Screenshot-2.png',
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 2523,
        'share_cnt': 32,
        'comment_cnt': 0
    },
    {
        'id': 6,
        'author': SampleUsers[3],
        'contents' : 'Designing my first ever social media website. So far, it\'s been fun! But maybe the smiling cubes are a little too silly?',
        'media' : 'post-media/VibeSpace-Screenshot.png',
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 3523,
        'share_cnt': 95,
        'comment_cnt': 0
    },
    {
        'id': 7,
        'author': SampleUsers[0],
        'contents' : 'This is an example of a group post.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 45,
        'share_cnt': 95,
        'comment_cnt': 0
    },
    {
        'id': 8,
        'author': SampleUsers[3],
        'contents' : 'Only posts made in the group will show up on the group page.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 15,
        'share_cnt': 95,
        'comment_cnt': 0
    }
]
SamplePostsInFeed = [SamplePosts[0], SamplePosts[1], SamplePosts[5]]
SampleGroupPosts = [SamplePosts[7], SamplePosts[8]]

ListsOfSamplePostsGroupedByAuthor = []
for SampleUser in SampleUsers:
    PostsUserMade = [post for post in SamplePosts if post["author"] == SampleUser and post not in SampleGroupPosts]
    ListsOfSamplePostsGroupedByAuthor.append(PostsUserMade)

SampleComments = [
    {
        'id': 0,
        'author': SampleUsers[2],
        'contents' : 'Hello, I am an example comment. I myself cannot be shared, directly commented on, or viewed in a separate page, but giving me a like would make me very happy!',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 3227,
        'share_cnt': None,
        'comment_cnt': None
    },
    {
        'id': 1,
        'author': SampleUsers[1],
        'contents' : '@sls0013 Don\'t beg for likes...',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 2755,
        'share_cnt': None,
        'comment_cnt': None
    },
    {
        'id': 2,
        'author': SampleUsers[2],
        'contents' : '@Adrian5234 I wasn\'t begging? I was just saying that likes make me happy.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 2180,
        'share_cnt': None,
        'comment_cnt': None
    },
    {
        'id': 3,
        'author': SampleUsers[1],
        'contents' : '@sls0013 Whatever. Likes don\'t matter anyways. At the end of the day, they are just worthless internet points.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 1795,
        'share_cnt': None,
        'comment_cnt': None
    },
    {
        'id': 4,
        'author': SampleUsers[2],
        'contents' : '@Adrian5234 Sure they don\'t matter? Because they say that if a reply gets more likes than what was replied to, people may take that very seriously!',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 4581,
        'share_cnt': None,
        'comment_cnt': None
    },
    {
        'id': 5,
        'author': SampleUsers[1],
        'contents' : '@sls0013 Man.',
        'media' : None,
        'date_time_posted': '2020-01-01 01:55:55',
        'like_cnt': 2822,
        'share_cnt': None,
        'comment_cnt': None
    }
]

# Schema for Group:
# Group = (id, name, description, group_pic, date_created, is_private, member_cnt)
SampleGroups = [
    { 
        'id': 0,
        'name': "Appreciate Nature!",
        'description': 'Get off of your chair! Plant a Tree! Go for a walk outside!',
        'group_pic': 'group-images/nature.png',
        'date_created': '2020-01-01',
        'is_private': False,
        'member_cnt': 1235,
        'group_creator' : SampleUsers[0]
    },
    { 
        'id': 1,
        'name': "FalseNoiseFans",
        'description': "Group for fans of the music artist False Noise",
        'group_pic': 'group-images/false-noise-serpentine.png',
        'date_created': '2020-01-01',
        'is_private': False,
        'member_cnt': 25,
        'group_creator' : SampleUsers[3]
    },
    { 
        'id': 2,
        'name': "ExampleDefaultGroup",
        'description': None,
        'group_pic': None,
        'date_created': '2020-01-01',
        'is_private': False,
        'member_cnt': 3,
        'group_creator' : SampleUsers[1]
    },
]

def addSampleGroupToModel(sample_group_index, group_creator_username):
    group = SampleGroups[sample_group_index]
    
    group_creator = VibeUser.objects.get(username=group_creator_username)
    
    newGroupRecord = VibeGroup.objects.create(
        id = group['id'],
        name = group['name'],
        date_created = group['date_created'],
        is_private = group['is_private'],
        member_cnt = group['member_cnt'],
        group_creator=group_creator
    )
    
    if group.get('description') is not None:
        newGroupRecord.description = group['description']
        
    if group.get('group_pic') is not None:
        newGroupRecord.group_pic = group['group_pic']
    
    newGroupRecord.save()
    
def addSampleUserToModel(sample_user_index):
    user = SampleUsers[sample_user_index]
    newUserRecord = VibeUser.objects.create(
        displayname = user['displayname'],
        username = user['username'],
        password = user['password'],
        bio = user['bio'],
        location = user['location'],
        email = user['email'],
        date_of_birth = user['date_of_birth'],
        follower_cnt = user['follower_cnt'],
        follows_cnt = user['follows_cnt'],
        post_cnt = user['post_cnt'],
        is_verified = user['is_verified']
    )
    
    if user.get('profile_pic') is not None:
        newUserRecord.profile_pic = user['profile_pic']
        
    if user.get('banner_pic') is not None:
        newUserRecord.banner_pic = user['banner_pic']
    
    newUserRecord.save()
    
def addSamplePostOrCommentToModel(sample_post_index, is_comment):
    if is_comment:
        post = SampleComments[sample_post_index]
    else:
        post = SamplePosts[sample_post_index]
    
    post_author_in_record = VibeUser.objects.get(username=post['author']['username'])
    
    if is_comment:
        post_replied_to = VibePost.objects.get(id=0)
        
        newUserRecord = VibeComment.objects.create(
            post_replied_to = post_replied_to,
            
            id = post['id'],
            author = post_author_in_record,
            contents = post['contents'],
            date_time_posted = post['date_time_posted'],
            like_cnt = post['like_cnt'],
            share_cnt = post['share_cnt'],
            comment_cnt = post['comment_cnt'],
        )
    else:
        newUserRecord = VibePost.objects.create(
            id = post['id'],
            author = post_author_in_record,
            contents = post['contents'],
            date_time_posted = post['date_time_posted'],
            like_cnt = post['like_cnt'],
            share_cnt = post['share_cnt'],
            comment_cnt = post['comment_cnt'],
        )
    
    if post.get('media') is not None:
        newUserRecord.media = post['media']
    
    newUserRecord.save()