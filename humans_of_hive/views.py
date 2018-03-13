from django.shortcuts import render
from django.contrib.auth import logout
from humans_of_hive.forms import PostForm, CommentForm, UserForm, UserProfileForm

def home(request):
    #home page

def about(request):
    return render(request, 'humans_of_hive/about.html', {})

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
            #display errors???
            print(user_form.errors, profile_form.errors)
    #If request is not HTTP POST
    else:
        #display registration form
        user_form=UserForm()
        profile_form=UserProfileForm()
    #Render the template with a content
    context_dict = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
    return render(request, 'humans_of_hive/register.html', context=context_dict)

def login(request):
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
                #send to home page!!!
            #if user is NOT active
            else:
                #block login and provide information
                context_dict={'message':'Your account is disabled./n If you are unsure why this happened, please contact us.'}
                return render(request, !!!path_back_to_login!!!, context=context_dict)
        #If there is no such user
        else:
            #display information
            context_dict = {'message': "Invalid login details supplied."}
            print ("Invalid login details: {0}, {1}".format(username, password))
            #allow for retry
            return render(request, !!!path_back_to_login!!!, context=context_dict)
    #If request is not HTTP POST,
    else:
        #display login page
        return render(request, !!!path_back_to_login!!!, {})

@login_required
def logout(request):
    #User is certainly logged on, so simply logout
    logout(request)
    #return to home !!!!!!!!!!!!!!!!!!!!!!

def show_post(request):
    #page for viewing posts

@login_required
def add_post(request):
    form = PostForm()
    #If request is HTTP POST
    if request.method=='POST':
        #indicate POST request to form
        form=CategoryForm(request.POST)
        #If forms is valid
        if form.is_valid():
            #save new post to the category
            form.save(commit=True)
            "GO TO USER / HOME PAGE; DISPLAY SUCCESS MESSAGE???"
        #If form is NOT valid
        else:
            #print out error message(s)
            print(form.errors)
    context_dict={'form':form}
    return render(request, !!!return_somewhere!!!, context=context_dict)

@login_required
def add_comment(request, category_name_slug):
    #Check if the page user is trying to comment actually exists
    try:
        post = Post.objects.get(slug=category_name_slug)
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
                "comment.time_posted = get now date"
                comment.save()
                "GO BACK TO THE POST"
        #If form is invalid or post does not exist
        else:
            #print errors
            print(form.errors)
    context_dict = {'form': form, 'post': post}
    return render(request, !!!go_to_the_post!!!, context_dict)

@login_required
def show_profile(request):
    #user profile page

@login_required
def user_posts(request):
    #page displaying all the posts of a given user

def hall_of_fame(request):
    #page displaying all posts with more the 50? points