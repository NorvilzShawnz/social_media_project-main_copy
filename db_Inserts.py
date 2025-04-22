#Welcome.
#This file is just for populating our database.
#I utilized actual SQL to insert, and made random
#objects for inserting. It worked perfectly!

#This first part was used to insert random users into our database

import os
import django
from django.db import connection
from django.contrib.auth.hashers import make_password
from datetime import date
import random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_project.settings")
django.setup()

first_names = [
    "Luca", "Sofia", "Jayden", "Aaliyah", "Mateo", "Isla", "Ezra", "Zoe",
    "Noah", "Amara", "Milo", "Leila", "Elio", "Nova", "Kai", "Luna", "Aria", "Ravi", "Emery", "Ayden"
]

last_names = [
    "Rivera", "Nguyen", "Patel", "Thompson", "Gomez", "Ali", "Lee", "Garcia",
    "Kim", "Martinez", "Hernandez", "Johnson", "Singh", "Brown", "Walker", "Clark", "Ramirez", "Torres", "Sharma", "Cooper"
]

bios = [
    "Living my best digital life 💻✨",
    "Coffee in hand, code on screen ☕️👩‍💻",
    "I’m the vibe 😌",
    "Messy but make it aesthetic",
    "Verified in my mind 💅",
    "Pixel princess with attitude",
]

locations = ["Miami", "Tallahassee", "New York", "L.A.", "Chicago", "Atlanta", "Paris", None]

default_password = make_password("vibespace123")

used_usernames = set()

def generate_unique_username(first, last):
    base = f"{first.lower()}.{last.lower()}"
    username = base
    count = 1
    while username in used_usernames:
        username = f"{base}{count}"
        count += 1
    used_usernames.add(username)
    return username

with connection.cursor() as cursor:
    for _ in range(20):
        first = random.choice(first_names)
        last = random.choice(last_names)
        displayname = f"{first} {last}"
        username = generate_unique_username(first, last)
        email = f"{username}@vibespace.com"
        profile_pic = "smiling-cube.png"
        banner_pic = "default-banner.png"
        bio = random.choice(bios)
        location = random.choice(locations)
        dob = date(random.randint(1997, 2005), random.randint(1, 12), random.randint(1, 28))

        follower_cnt = random.randint(0, 500)
        follows_cnt = random.randint(0, 500)
        post_cnt = random.randint(0, 100)
        is_verified = random.choice([True, False])

        cursor.execute("""
            INSERT INTO core_vibeuser (
                password, last_login, is_superuser, username, first_name, last_name, email,
                is_staff, is_active, date_joined, displayname, profile_pic, banner_pic, bio,
                location, date_of_birth, follower_cnt, follows_cnt, post_cnt, is_verified
            ) VALUES (
                %s, NULL, FALSE, %s, %s, %s, %s, FALSE, TRUE, CURRENT_TIMESTAMP,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """, [
            default_password, username, first, last, email, displayname, profile_pic, banner_pic, bio,
            location, dob, follower_cnt, follows_cnt, post_cnt, is_verified
        ])



#This portion is for populating the posts.
#It made a random image per post, and used our unique
#users to post them


import os
import django
from django.db import connection
import urllib.request
import random
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_project.settings")
django.setup()

# Step 1: Generate 30 unique images using https://picsum.photos
MEDIA_DIR = "media/post-media"
os.makedirs(MEDIA_DIR, exist_ok=True)

image_filenames = []

for i in range(1, 31):
    filename = f"unique{i}.jpg"
    filepath = os.path.join(MEDIA_DIR, filename)
    url = f"https://picsum.photos/seed/vibe{i}/600/600"
    if not os.path.exists(filepath):
        urllib.request.urlretrieve(url, filepath)
    image_filenames.append(f"post-media/{filename}")

# Step 2: Unique captions/bios for each post
captions = [
    "Sunset vibes only 🌇",
    "Grind mode: activated 💼⚡",
    "Becoming the person I needed as a kid ✨",
    "Weekend reset 🌿📖",
    "Catch flights, not feelings 🛫💔",
    "IDK, felt cute 🫠",
    "Building dreams, one bug at a time 🐛👨‍💻",
    "She’s beauty, she’s grace, she has resting dev face 😎",
    "Mood: headphones in, world out 🎧",
    "I post, therefore I am 💭📸",
    "Do not disturb: self care in progress 🧖‍♀️",
    "Too glam to give a damn 💄",
    "Escaping the matrix... brb ⌛",
    "Soft light and softer hearts 🕊️",
    "CTRL+C my aesthetic 📎",
    "Main feed magic only 🪄",
    "Here to romanticize everything 💐",
    "Digital detox complete ✅",
    "Doing the most, as always 💅",
    "Talk to me nice or not at all 💬",
    "A little chaos, a lot of coffee ☕",
    "Smiling through it all 😌",
    "On my clean girl arc 🧼",
    "Gave a vibe and left 💨",
    "Living for the plot 📖",
    "Golden hour never misses ✨",
    "Trust the pixels 📷",
    "Cozy coding season 🔥",
    "Just another pretty variable 🧠💖",
    "Post and disappear 🕵️"
]

# Step 3: Get all users and assign posts randomly
with connection.cursor() as cursor:
    cursor.execute("SELECT id FROM core_vibeuser")
    users = [row[0] for row in cursor.fetchall()]

    post_count = min(len(users), 30)  # One post per user (max 30 posts)

    for i in range(post_count):
        author_id = random.choice(users)
        users.remove(author_id)  # Avoid duplicates if possible

        contents = captions[i]
        media = image_filenames[i]
        date_posted = datetime.now() - timedelta(days=random.randint(0, 30))
        like_cnt = random.randint(0, 300)
        share_cnt = random.randint(0, 100)
        comment_cnt = random.randint(0, 50)

        cursor.execute("""
            INSERT INTO core_vibepost (
                author_id, contents, media, date_time_posted, like_cnt, share_cnt, comment_cnt
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            author_id, contents, media, date_posted, like_cnt, share_cnt, comment_cnt
        ])



#this inserts comments!


import os
import django
from django.db import connection
import urllib.request
import random
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_project.settings") 
django.setup()

# Step 1: Download 10 gif files into media/comment-media
MEDIA_DIR = "media/comment-media"
os.makedirs(MEDIA_DIR, exist_ok=True)

gif_urls = {
    f"gif{i+1}.gif": f"https://media.giphy.com/media/{gid}/giphy.gif" for i, gid in enumerate([
        "3o7aD2saalBwwftBIY",  # eye roll
        "26ufdipQqU2lhNA4g",  # clapping
        "3oKIPwoeGErMmaI43C",  # girl please
        "1iTHHR7XCzz6I",       # confused
        "l0IylOPCNkiqOgMyA",   # excited jump
        "13gvXfEVlxQjDO",      # yawn
        "5GoVLqeAOo6PK",       # sparkly vibes
        "3o6Zt481isNVuQI1l6",  # dramatic zoom
        "3orieRYpP3Zz5OYYNa",  # duck walks away
        "l0MYt5jPR6QX5pnqM"    # intense stare
    ])
}

for filename, url in gif_urls.items():
    filepath = os.path.join(MEDIA_DIR, filename)
    if not os.path.exists(filepath):
        urllib.request.urlretrieve(url, filepath)

# Step 2: Comment text bank
comment_texts = [
    "Obsessed with this 🔥",
    "ok but this pic >>>",
    "Giving everything it needs to give 😮‍💨",
    "You ate this up tbh",
    "Drop the routine pls 😩",
    "The vibes are immaculate",
    "She’s THAT girl 🫦",
    "This is a whole mood",
    "Kinda obsessed ngl",
    "Living for this post 💯",
    "Omg where is this from??",
    "Internet-breaking energy",
    "Saving this forever 💾",
    "The caption??? Genius",
    "Why are you always so cute 😤",
    "Teach me your ways",
    "Literally perfect",
    "I needed to see this today 😭",
    "10/10 would double tap again",
    "Vibes unmatched 🌀",
    "Honestly? Iconic.",
    "Your feed > everyone else's",
    "I’m crying this is too good 😭",
    "This deserves more likes",
    "Okayyy who’s the photographer?",
    "Giving main character",
    "It’s giving Pinterest board",
    "Can’t stop looking at this",
    "Art. Literally art.",
    "That filter goes crazy",
    "Stop I’m screaming 😂",
    "Ugh you're so cool",
    "This lives rent free in my head",
    "No one’s doing it like you",
    "Bookmarking this rn",
    "Shaking crying throwing up",
    "Need this framed",
    "This? A masterpiece.",
    "Can’t compete with that",
    "Lowkey in love with this post"
]

# Step 3: Seeding 40 comments, 10 of them with gifs
with connection.cursor() as cursor:
    cursor.execute("SELECT id FROM core_vibepost")
    posts = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id FROM core_vibeuser")
    users = [row[0] for row in cursor.fetchall()]

    gif_filenames = list(gif_urls.keys())
    gif_indices = random.sample(range(40), 10)  # pick 10 indexes that will have gifs

    used_pairs = set()

    for i in range(40):
        post_id = random.choice(posts)
        author_id = random.choice(users)

        # Avoid users commenting on their own post
        if (post_id, author_id) in used_pairs:
            continue
        used_pairs.add((post_id, author_id))

        contents = comment_texts[i]
        media = None

        if i in gif_indices:
            media = f"comment-media/{gif_filenames.pop()}"

        date_posted = datetime.now() - timedelta(days=random.randint(0, 30))
        like_cnt = random.randint(0, 100)
        share_cnt = random.randint(0, 20)
        comment_cnt = random.randint(0, 10)

        cursor.execute("""
            INSERT INTO core_vibecomment (
                post_replied_to_id, author_id, contents, media, date_time_posted,
                like_cnt, share_cnt, comment_cnt
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            post_id, author_id, contents, media, date_posted,
            like_cnt, share_cnt, comment_cnt
        ])


#Lastly, to insert more groups!


import os
import django
from django.db import connection
import urllib.request
import random
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_project.settings")
django.setup()

# Step 1: Download a few group images
MEDIA_DIR = "media/group-images"
os.makedirs(MEDIA_DIR, exist_ok=True)

group_images = {
    f"group{i+1}.png": f"https://picsum.photos/seed/group{i+1}/300/300" for i in range(6)
}

for filename, url in group_images.items():
    filepath = os.path.join(MEDIA_DIR, filename)
    if not os.path.exists(filepath):
        urllib.request.urlretrieve(url, filepath)

image_filenames = list(group_images.keys())

# Step 2: Group names + descriptions
group_names = [
    "Code Coven", "Late Night Lounge", "Digital Dreamers", "Finsta Family", "Vibe Core",
    "Main Character Energy", "Lowkey Legends", "Post No Pics", "Pixel Party",
    "Scroll Survivors", "Cloud Club", "Chill Frequency"
]

descriptions = [
    "For the realest ones only.",
    "Share memes, chaos, and digital love.",
    "A space to dump your brain and your feed.",
    "Where we talk in lowercase only.",
    "No judgment, just vibes.",
    "Coding, crying, thriving.",
    "For when you just need a group chat rant.",
    "An archive of nothing and everything.",
    "We go live at midnight.",
    "Lurkers welcome.",
    "Private vibes only.",
    "A safe space for main characters."
]

# Step 3: Get user IDs to randomly assign as creators
with connection.cursor() as cursor:
    cursor.execute("SELECT id FROM core_vibeuser")
    users = [row[0] for row in cursor.fetchall()]

    for i in range(12):
        name = group_names[i]
        description = descriptions[i]
        group_pic = f"group-images/{random.choice(image_filenames)}"
        is_private = random.choice([True, False])
        member_cnt = random.randint(1, 20)
        creator_id = random.choice(users)

        cursor.execute("""
            INSERT INTO core_vibegroup (
                name, description, group_pic, date_created, is_private, member_cnt, group_creator_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [
            name, description, group_pic, date.today(), is_private, member_cnt, creator_id
        ])

