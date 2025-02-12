

from django.shortcuts import render, get_object_or_404
from home.models import Post

def home(request):
    posts = Post.objects.all()  # Fetch all posts instead of one
    return render(request, 'home.html', {'posts': posts})
