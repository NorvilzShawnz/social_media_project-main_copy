# Generated by Django 5.1.7 on 2025-04-21 03:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_vibegroup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vibeuser',
            name='banner_pic',
            field=models.ImageField(default='default-banner.png', upload_to='banners'),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='displayname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='follower_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='follows_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='location',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='post_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vibeuser',
            name='profile_pic',
            field=models.ImageField(default='smiling-cube.png', upload_to='profile-images'),
        ),
        migrations.AlterField(
            model_name='vibegroup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='VibePost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.TextField(blank=True, null=True)),
                ('media', models.ImageField(blank=True, null=True, upload_to='post-media')),
                ('date_time_posted', models.DateTimeField(auto_now_add=True)),
                ('like_cnt', models.IntegerField(default=0)),
                ('share_cnt', models.IntegerField(default=0)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
