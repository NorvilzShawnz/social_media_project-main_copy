from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VibeUser, VibeGroup, VibePost, VibeComment

admin.site.register(VibeUser, UserAdmin)
admin.site.register(VibeGroup)
admin.site.register(VibePost)
admin.site.register(VibeComment)
