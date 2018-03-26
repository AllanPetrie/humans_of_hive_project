from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from humans_of_hive.models import Post,Comment,UserProfile,Follow
from humans_of_hive.forms import PostForm,CommentForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required
from datetime import datetime
from django.contrib.auth.models import User

'''
List of views for convenience:
-home
-about
-register
-user_login
-logout
-show_post
-add_post
-add_comment
-show_profile
-user_posts
-hall_of_fame
-all_users ?????
-follower_add
-follower_remove
-followers_list
-following_list
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
        user = UserProfile.objects.get(user=post.user.user).slug
        #populate context dictionary
        context_dict['post'] = post
        context_dict['comments'] = comments
        context_dict['user'] = user
    except Post.DoesNotExist:
        #populate context dictionary
        context_dict['user'] = None
        context_dict['post'] = None
        context_dict['comments'] = None
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

#@login_required
#def show_profile(request, user_name_slug):
#    context_dict = {}
#    try:
#        #get the requested user
#        user_profile = UserProfile.objects.get(slug=user_name_slug)
#        #update context dictionary
#        context_dict['user_profile'] = user_profile
#    except UserProfile.DoesNotExist:
#        #update context dictionary
#        context_dict['user_profile'] = None
#    return render(request, 'humans_of_hive/user_profile.html', context=context_dict)

@login_required
def show_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context_dict = {'user_profile': user_profile}
    return render(request, 'humans_of_hive/user_profile.html', context=context_dict)


@login_required
def user_posts(request):
    #Get current user
    current_user = request.user
    #get posts by current user
    posts = Post.objects.filter(user=current_user)
    context_dict = {'posts':posts}
    return render(request, 'humans_of_hive/user_posts.html', context=context_dict)

def hall_of_fame(request):
    fame_list = Post.objects.order_by('-points')[:10]
    context_dict = {'posts' : fame_list}
    return render(request, 'humans_of_hive/hall_of_fame.html', context=context_dict)

@login_required
def all_users(request):
    users = User.objects.filter(fieldname='searchterm')
    #Get all usernames of registered users
    context_dict = {'users': users.values_list('username', flat=True)}
    return render(request, 'humans_of_hive/users.html', context=context_dict)

@login_required
def follow(request, user_name_slug):
    #If it is a POST request
    if request.method == 'POST':
        #get user that current user wants to follow
        followee = UserProfile.objects.get(slug=user_name_slug).user
        context_dict = {'followee_username': followee.username}
        follower = request.user
        try:
            Follow.objects.add_follower(follower, followee)
        #if that user is already being followed
        except AlreadyExistsError as e:
            #add error to context dictionary
            context_dict['errors'] = ['%s' % e]
    return render(request, 'humans_of_hive/add_follower.html', context=context_dict)

@login_required
def follower_remove(request, followee_username):
    #If it is a POST request
    if request.method == 'POST':
        #get user that is to be removed
        followee = User.objects.get(username=followee_username)
        follower = request.user
        #remove user
        Follow.objects.remove_follower(follower, followee)
        #TODO: 'friendship_following' to be replaced by suitable url
        return redirect('friendship_following', username=follower.username)
    context_dict = {'followee_username': followee_username}
    return render(request, 'humans_of_hive/remove_follower.html', context=context_dict)

def followers_list(request, username):
    #Get user whose followers are to be listed
    user = User.objects.filter(username=username)
    #collect all the followers of that user
    followers = Follow.objects.followers(user)
    context_dict = {'username': user.username, 'followers': followers}
    return render(request, 'humans_of_hive/followers_list.html', context=context_dict)

def following_list(request, username):
    #Get user whose followed users are to be listed
    user = User.objects.filter(username=username)
    #collect all the users followed
    following = Follow.objects.following(user)
    context_dict = {'username': user.username, 'following': following}
    return render(request, 'humans_of_hive/following_list.html', context=context_dict)
