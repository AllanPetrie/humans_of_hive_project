from django.shortcuts import render

def home(request):
    #home page

def about(request):
    return render(request, 'humans_of_hive/about.html', {})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        

def login(request):
    #login page

def show_post(request):
    #page for viewing posts

def add_post(request):
    #page for creating a posts

def add_comment(request):
    #page for creating a comment

def show_profile(request):
    #user profile page

def user_posts(request):
    #page displaying all the posts of a given user

def hall_of_fame(request):
    #page displaying all posts with more the 50? points
