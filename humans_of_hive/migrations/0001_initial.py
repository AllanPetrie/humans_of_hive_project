# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 13:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['time_posted', 'owner'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManageFollows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('story', models.CharField(max_length=999999)),
                ('picture', models.ImageField(blank=True, upload_to='post_photos')),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
                ('level_of_study', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='humans_of_hive.UserProfile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='followee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='humans_of_hive.UserProfile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='humans_of_hive.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='humans_of_hive.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='humans_of_hive.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'followee')]),
        ),
    ]