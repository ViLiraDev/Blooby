from django.shortcuts import render
from .models import Profile, Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'feed.html',context)