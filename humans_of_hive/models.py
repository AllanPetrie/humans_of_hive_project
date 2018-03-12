from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Post(models.model):
    title = models.CharField(max_length = 100)
    points = models.IntegerField(default = 0)
    story = models.CharField(max_length = 999999) #max length subject to change
    picture = models.ImageField(upload_to='post_photos', blank=True) #is it possible to make photos optional?
    #time_posted = models.DateTimeField????


    """
    Not sure if a save method is needed
    """

    def __str__(self):
        return self.title

class Comment(models.model):
    post = models.ForeignKey(Post)
    content = models.CharField(max_length = 1000)
    #time_posted = models.DateTimeField????
    #field to store the user that created the comment?

    def __str__(self):
        #what should we use for this?



class UserProfile(models.model):
    user = models.OneToOneField(User)
