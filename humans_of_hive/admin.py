from django.contrib import admin
from humans_of_hive.models import Post, Comment, UserProfile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
