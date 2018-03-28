from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from humans_of_hive.models import Post,Comment,UserProfile,Follow,FollowingManager
from humans_of_hive.forms import PostForm,CommentForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.db import IntegrityError

'''
List of views for convenience:
-home
-about
-register
-user_login
-user_logout
-show_post
-add_post
-add_comment
-show_profile
-user_posts
-hall_of_fame
-follow
-unfollow
-like_post
'''

def home(request):
    post_list = Post.objects.order_by('-time_posted')
    context_dict = {'info': 'Nullamlacus dui ipsum conseque loborttis non euisque morbi penas dapibulum orna. '
                            'Urnaultrices quis curabitur phasellentesque congue magnis vestibulum quismodo nulla et feugiat adipiscinia pellentum leo.',
                    'posts': post_list}
    return render(request, 'humans_of_hive/home.html', context=context_dict)

def about(request):
    information = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sodales eros sit amet mattis vulputate. Vivamus porta vestibulum sem\
    ut auctor. Morbi felis nulla, iaculis et aliquam non, rutrum eu felis. Integer sed metus ipsum. Fusce sit amet aliquam mauris.\
    Aenean sollicitudin faucibus velit, vel molestie leo iaculis ac. Curabitur vulputate mi ante, nec aliquet elit tempus eu. Integer\
    sed neque mattis, ullamcorper sapien quis, interdum risus. Pellentesque vel sodales purus, eu blandit magna. Nunc nec interdum\
    ipsum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed at bibendum leo, sit amet placerat risus. Quisque et\
    iaculis sem, non facilisis nulla. Maecenas in molestie tortor. Morbi consectetur at est vel hendrerit.'
    context_dict = {'info': information, 'owners': ['Allan Petrie', 'Andrew Craig', 'Jonathan Henderson', 'Marija Vaskeviciute']}
    return render(request, 'humans_of_hive/about.html', context=context_dict)

def register(request):
    #Set registered to False to indicate that registration is ongoing
    registered = False
    #If request is HTTP POST, process information
    if request.method == "POST":
        #Take information from the forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        #If forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            #save user to database
            user=user_form.save()
            #hash password
            user.set_password(user.password)
            #update user object
            user.save()
            #save profile model with time delay to avoid integrity problems
            profile=profile_form.save(commit=False)
            #set the user attribute 'manually'
            profile.user=user
            #If user provided profile picture
            if 'profile_picture' in request.FILES:
                #get it form form and put into user profile model
                profile.picture = request.FILES['profile_picture']
            #save profile
            profile.save()
            #set registered to True to indicate successful registration
            registered=True
            new_user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'],)
            login(request, new_user)
            return HttpResponseRedirect('/humans_of_hive/')
        #If incorrect details were provided
        else:
            print(user_form.errors, profile_form.errors)
    #If request is not HTTP POST
    else:
        #display registration form
        user_form=UserForm()
        profile_form=UserProfileForm()
    #Render the template with a content
    context_dict = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
    return render(request, 'humans_of_hive/register.html', context=context_dict)

def user_login(request):
    #If request is HTTP POST
    if request.method=='POST':
        #get information from the user
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check that provided information is correct
        user=authenticate(username=username, password=password)
        #If such user exists
        if user:
            #if the user is active
            if user.is_active:
                #allow the login
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            #if user is NOT active
            else:
                #block login and provide information
                context_dict={'message':'Your account is disabled./n If you are unsure why this happened, please contact us.'}
                return render(request, 'humans_of_hive/login.html', context=context_dict)
        #If there is no such user
        else:
            #display information
            context_dict = {'message': "Invalid login details supplied."}
            print ("Invalid login details: {0}, {1}".format(username, password))
            #allow for retry
            return render(request, 'humans_of_hive/login.html', context=context_dict)
    #If request is not HTTP POST,
    else:
        #display login page
        return render(request, 'humans_of_hive/login.html', {})

@login_required
def user_logout(request):
    #User is certainly logged on, so simply logout
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def show_post(request, post_name_slug):
    context_dict = {}
    try:
        #get the requested post
        post = Post.objects.get(slug=post_name_slug)
        #get comments of that post
        comments = Comment.objects.filter(post=post)
        #get slug for user that created a post
        user = UserProfile.objects.get(user=post.user.user)
        if request.user.is_authenticated():
            follower = UserProfile.objects.get(user=request.user)
            follows = Follow.follow_objects.follows(follower=follower, followee=user)
            context_dict['follows'] = follows
        else:
            context_dict['follows'] = None
        #populate context dictionary
        context_dict['post'] = post
        context_dict['comments'] = comments
        context_dict['user'] = user.slug
    except Post.DoesNotExist:
        #populate context dictionary
        context_dict['user'] = None
        context_dict['post'] = None
        context_dict['comments'] = None
        context_dict['follows'] = None
    return render(request, 'humans_of_hive/view_post.html', context=context_dict)

@login_required
def add_post(request):
    form = PostForm()
    #If request is HTTP POST
    if request.method=='POST':
        #indicate POST request to form
        form=PostForm(request.POST)
        #If forms is valid
        if form.is_valid():
            #save new post to the category
            post=form.save(commit=False)
            #set user value
            post.user = UserProfile.objects.get(user=request.user)
            post.save()
            return home(request)
        #If form is NOT valid
        else:
            #print out error message(s)
            print(form.errors)
    context_dict={'form':form}
    return render(request, 'humans_of_hive/add_post.html', context=context_dict)

@login_required
def add_comment(request, post_name_slug):
    #Check if the page user is trying to comment actually exists
    try:
        post = Post.objects.get(slug=post_name_slug)
    except Post.DoesNotExist:
        post=None
    #Get form comment
    form = CommentForm()
    #If request is HTTP POST
    if request.method=='POST':
        #indicate POST request to the form
        form = CommentForm(request.POST)
        #If form is valid
        if form.is_valid():
            #If post exists
            if post:
                #save comment model with time delay to avoid integrity problems
                comment=form.save(commit=False)
                #set values in the model
                comment.post = post
                user_profile = UserProfile.objects.get(user=request.user)
                comment.owner = user_profile
                comment.save()
                return show_post(request, post_name_slug)
        #If form is invalid or post does not exist
        else:
            #print errors
            print(form.errors)
    context_dict = {'form': form, 'post': post}
    return render(request, 'humans_of_hive/add_comment.html', context_dict)

@login_required
def show_profile(request):
    #Get user whose profile is to be displayed
    user_profile = UserProfile.objects.get(user=request.user)
    context_dict = {'user_profile': user_profile, 'path': 'user_profile'}
    #Check if profile image exists
    if not user_profile.profile_picture:
        context_dict['image_exists'] = [False]
    else:
        context_dict['image_exists'] = [True]
    # collect all the followers of that user
    followers = Follow.follow_objects.followers(user_profile)
    context_dict['followers'] = [followers]
    # collect all the users followed by them
    following = Follow.follow_objects.following(user_profile)
    context_dict['following'] = [following]
    return render(request, 'humans_of_hive/user_profile.html', context=context_dict)

@login_required
def user_posts(request, user_name_slug):
    #Get user whose posts are to displayed
    user = UserProfile.objects.get(slug=user_name_slug)
    #get posts by that user
    posts = Post.objects.filter(user=user)
    context_dict = {'posts':posts, 'owner':user}
    return render(request, 'humans_of_hive/user_posts.html', context=context_dict)

def hall_of_fame(request):
    fame_list = Post.objects.order_by('-points')[:10]
    context_dict = {'posts' : fame_list}
    return render(request, 'humans_of_hive/hall_of_fame.html', context=context_dict)

@login_required
def follow(request, post_name_slug, user_name_slug):
    followee = UserProfile.objects.get(slug=user_name_slug)
    follower = UserProfile.objects.get(user=request.user)
    context_dict = {'followee': followee, 'follower': follower}
    if request.method == 'POST':
        try:
            Follow.follow_objects.add_follower(follower, followee)
            return show_post(request, post_name_slug)
        #if that user is already being followed
        except IntegrityError as e:
            #add error to context dictionary
            context_dict['errors'] = ['%s' % e]
    return render(request, 'humans_of_hive/add_follower.html', context=context_dict)

@login_required
def unfollow(request, user_name_slug, post_name_slug):
    followee = UserProfile.objects.get(slug=user_name_slug)
    follower = UserProfile.objects.get(user=request.user)
    context_dict = {'followee': followee, 'follower': follower}
    #If it is a POST request
    if request.method == 'POST':
        #remove user
        Follow.follow_objects.remove_follower(follower, followee)
        if post_name_slug == 'user_profile':
            return show_profile(request)
        else:
            return show_post(request, post_name_slug)
    return render(request, 'humans_of_hive/remove_follower.html', context=context_dict)

@login_required
def like_post(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']
    points = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            points = post.points + 1
            post.points =  points
            post.save()
    return HttpResponse(points)

