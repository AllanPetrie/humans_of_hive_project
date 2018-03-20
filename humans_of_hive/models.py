from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    degree = models.CharField(max_length = 50)
    level_of_study = models.CharField(max_length = 20)
    profile_picture = models.ImageField(upload_to = 'profile_images', blank = True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title_length = 100
    story_length = 999999#max length subject to change
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length = title_length)
    points = models.IntegerField(default = 0)
    story = models.CharField(max_length = story_length)
    picture = models.ImageField(upload_to='post_photos', blank=True)
    time_posted = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank=True, unique=True)

    #we want people to be able to create new/access posts in our web page
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_length = 1000
    post = models.ForeignKey(Post)
    content = models.CharField(max_length = comment_length)
    time_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time_posted) + " " + self.content
