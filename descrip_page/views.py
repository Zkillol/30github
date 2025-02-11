from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from descrip_page.models import Comments
from home.models import Post

def comments(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, post_id=id)
        comments = Comments.objects.filter(post=post).order_by('-id')  # Filter comments for the post

        context = {
            'title': 'Подробнее о жилищах',
            'post': post,
            'comments': comments
        }
        return render(request, 'descrip_page.html', context)

    else:
        messages.error(request, "You Must Be Logged In To View This Page...")
        return redirect('home')
