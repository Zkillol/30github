from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from descrip_page.models import Comments
from home.models import Post


def comments(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404( Post ,post_id =id)
        return render(request, 'descrip_page.html', {'title': 'Главная страница сайта', 'post': post})
        comments = Comments.objects.order_by('-id')
        return render(request, 'descrip_page.html', {'title': 'Подробнее о жилищах', 'comments': comments})

    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')
