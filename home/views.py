
from django.shortcuts import render
from home.models import Post

def home(request):
    post = Post.objects.order_by('id')
    return render(request, 'home.html', {'title': 'Главная страница сайта', 'post': post})
