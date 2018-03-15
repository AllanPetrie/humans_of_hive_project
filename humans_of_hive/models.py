from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    title_length = 100
    story_length = 999999#max length subject to change
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length = title_length)
    points = models.IntegerField(default = 0)
    story = models.CharField(max_length = story_length)
    picture = models.ImageField(upload_to='post_photos', blank=True) #is it possible to make photos optional? 
    time_posted = models.DateTimeField
    slug = models.SlugField(blank=True, unique=True)

    #we want people to be able to create new/access posts in our web page
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_length = 1000
    post = models.ForeignKey(Post)
    content = models.CharField(max_length = comment_length)
    time_posted = models.DateTimeField
    #field to store the user that created the comment?

    def __str__(self):
        #what should we use for this?
        #maybe title of the post and comment.time_posted?

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    degree = models.CharField(max_length = 50)
    level_of_study = models.CharField(max_length = 20)
    profile_picture = models.ImageField(upload_to = 'profile_images', blank = True)

    def __str__(self):
        return self.user.username
