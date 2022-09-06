from django.contrib import admin
from .models import Profile, Post, Comment
from chats.models import ChatMessage,Thread
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ChatMessage)
admin.site.register(Thread)
