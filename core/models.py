from django.contrib.auth.models import AbstractUser
from django.db import models

class VibeUser(AbstractUser):
    email = models.EmailField(unique=True)
    displayname = models.CharField(max_length=20, default="")
    profile_pic = models.ImageField(upload_to="profile-images", default="smiling-cube.png")
    banner_pic = models.ImageField(upload_to="banners", default="default-banner.png")
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=35, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    follower_cnt = models.IntegerField(default=0)
    follows_cnt = models.IntegerField(default=0)
    post_cnt = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class VibePost(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(VibeUser, on_delete=models.CASCADE)
    contents = models.TextField(null=True, blank=True)
    media = models.ImageField(upload_to="post-media", null=True, blank=True)
    date_time_posted = models.DateTimeField(auto_now_add=True)
    like_cnt = models.IntegerField(default=0)
    share_cnt = models.IntegerField(default=0, null=True, blank=True)
    comment_cnt = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.author.username) + ' ' + self.contents[:75]

class VibeComment(models.Model):
    # This model has all attributes VibePost has, plus post_replied_to
    post_replied_to = models.ForeignKey(VibePost, on_delete=models.CASCADE)
    
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(VibeUser, on_delete=models.CASCADE)
    contents = models.TextField(null=True, blank=True)
    media = models.ImageField(upload_to="post-media", null=True, blank=True)
    date_time_posted = models.DateTimeField(auto_now_add=True)
    like_cnt = models.IntegerField(default=0)
    share_cnt = models.IntegerField(default=0, null=True, blank=True)
    comment_cnt = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.author.username) + ' ' + self.contents[:75]

class VibeGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500, default="No Description Provided")
    group_pic = models.ImageField(upload_to="group-images", default="smiling-cube.png")
    date_created = models.DateField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    member_cnt = models.IntegerField(default=1)
    group_creator = models.ForeignKey(VibeUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + ' ' + self.name