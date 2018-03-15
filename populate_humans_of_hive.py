import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'humans_of_hive_project.settings')

import django
django.setup()
from humans_of_hive.models import Post, Comment, User

def populate():

    posts = [
        {'title':"",
         ''},
        {},
        {},
        ]
