from django import forms
from django.contrib.auth.models import User
from humans_of_hive.models import Post, Comment, UserProfile

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.title_length, help_text='Name your post')
    points = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    story = forms.CharField(max_length=Post.story_length, help_text='Tell your story')
    picture = forms.ImageField(help_text='Add a picture')
    "time_posted = forms.DateTimeField(widget=forms.HiddenInput()) get now time"
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        #choose model to use
        model = Post
        #display fields to be set by the user
        fields = ('title', 'story', 'picture')

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=Comment.comment_length, help_text='Comment')
    "time_posted = forms.DateTimeField(widget=forms.HiddenInput()) get now time"
    class Meta:
        #choose model to use
        model = Comment
        #fields that are not to be displayed
        exclude = ('time_posted',)

class UserForm(forms.ModelForm):
    #hide password while it is typed
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        #choose model to use
        model=User
        #display fields that can be changed
        fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        #choose model to use
        model=UserProfile
        #display fields that allow input
        fields=('degree', 'level_of_study', 'profile_picture')
