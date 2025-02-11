

from django.shortcuts import render
from home.models import Post

def home(request):
    posts = Post.objects.all()  # ✅ Make sure post_id exists in the database
    return render(request, 'home.html', {'posts': posts})

