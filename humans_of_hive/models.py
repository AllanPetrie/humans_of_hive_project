from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#RELATIONSHIP_FOLLOWING = 1
#RELATIONSHIP_BLOCKED = 2
#RELATIONSHIP_STATUSES = ( (RELATIONSHIP_FOLLOWING, 'Following'), (RELATIONSHIP_BLOCKED, 'Blocked'), )

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    degree = models.CharField(max_length = 50)
    level_of_study = models.CharField(max_length = 20)
    profile_picture = models.ImageField(upload_to = 'profile_images', blank = True)
    #follows = models.ManyToManyField('self', through=Relationship, symmetric =False, related_name='related_to')

    def __str__(self):
        return self.user.username

    class Meta:
        #impose ordering on a UserProfile list
        ordering = ['user']

#class Relationship(models.Model):
#    from_user = models.ForeignKey(UserProfile, related_name='from_users')
#    to_user = models.ForeignKey(UserProfile, related_name='to_users')
#    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

class Post(models.Model):
    title_length = 100
    story_length = 999999
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length = title_length)
    points = models.IntegerField(default = 0)
    story = models.CharField(max_length = story_length)
    picture = models.ImageField(upload_to='post_photos', blank=True)
    time_posted = models.DateTimeField(auto_now_add = True)
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
    time_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.owner) +" "+ str(self.post)+" "+ str(self.time_posted)

    class Meta:
        #impose ordering on a comment list
        ordering = ['time_posted', 'owner']
