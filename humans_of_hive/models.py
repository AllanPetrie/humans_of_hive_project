from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
from django.db import IntegrityError
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    degree = models.CharField(max_length = 50)
    level_of_study = models.CharField(max_length = 20)
    profile_picture = models.ImageField(upload_to = 'images/', blank = True, null=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        #impose ordering on a UserProfile list
        ordering = ['user']

class FollowingManager(models.Model):
    #Get a list of all those following a user
    #Note: function expects a UserProfile instance
    @staticmethod
    def followers(user):
        followers = []
        if not Follow.objects.filter(followee=user):
            followers = None
        else:
            follower_users = Follow.objects.filter(followee=user).values_list('follower')
            for follower in follower_users:
                follower_user = UserProfile.objects.get(pk=follower[0])
                followers.append(follower_user)
        return followers

    #Get a list of all users a user is following
    #Note: function expects a UserProfile instance
    @staticmethod
    def following(user):
        following = []
        if not Follow.objects.filter(follower=user):
            following = None
        else:
            followees_users = Follow.objects.filter(follower=user).values_list('followee')
            for followee in followees_users:
                followed_user = UserProfile.objects.get(pk=followee[0])
                following.append(followed_user)
        return following

    #Check if user is following another user
    #Note: expects UserProfile instances
    @staticmethod
    def follows(follower, followee):
        try:
            Follow.objects.get(follower=follower, followee=followee)
            return True
        except Follow.DoesNotExist:
            return False

    # Add a new follower follows followee relationship
    #Note: expects UserProfile instances
    @staticmethod
    def add_follower(follower, followee):
        relation, created = Follow.objects.get_or_create(follower=follower, followee=followee)
        if not created:
            raise IntegrityError('User %s already follows %s' % (follower, followee))
        return relation

    #Remove follower follows followee relationship
    #Note: expects UserProfile instances
    @staticmethod
    def remove_follower(follower, followee):
        try:
            follow = Follow.objects.get(follower=follower, followee=followee)
            follow.delete()
            return True
        except Follow.DoesNotExist:
            return False

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following')
    followee = models.ForeignKey(UserProfile, related_name='followers')
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    follow_objects = FollowingManager()

    def save(self, *args, **kwargs):
        if self.follower == self.followee:
            raise IntegrityError('You cannot follow yourself')
        super(Follow, self).save(*args, **kwargs)

    def __str__(self):
        return "User %s follows %s" % (self.follower.user.username, self.followee.user.username)

    class Meta:
        unique_together = ('follower', 'followee')

class Post(models.Model):
    title_length = 100
    story_length = 999999
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length = title_length)
    points = models.IntegerField(default = 0)
    story = models.CharField(max_length = story_length)
    picture = models.ImageField(upload_to='post_photos', blank=True, null=True)
    time_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        #impose ordering on a posts list
        ordering = ['title']

class Comment(models.Model):
    comment_length = 1000
    owner = models.ForeignKey(UserProfile, default=None)
    post = models.ForeignKey(Post)
    content = models.CharField(max_length = comment_length)
    time_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner) +" "+ str(self.post)+" "+ str(self.time_posted)

    class Meta:
        #impose ordering on a comment list
        ordering = ['time_posted', 'owner']
