# Generated by Django 5.1.7 on 2025-04-21 09:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_vibepost_comment_cnt_alter_vibepost_share_cnt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vibegroup',
            name='group_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
