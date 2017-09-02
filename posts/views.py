from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostCreationForm
from datetime import datetime

def index(request):
    posts = Post.objects.all()
    return render(request, './posts/index.html', {'posts': posts})


def details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    comments_form = CommentForm()
    return render(request, './posts/post.html', {'post': post, 'comments': comments, 'form': comments_form})


@login_required(login_url='login')
def create_post(request):
    form = PostCreationForm()

    if request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.creation_date = datetime.now()
            new_post.save()
            return redirect('home')

    return render(request, './posts/create_post.html', {
        'form': form,
    })


@login_required(login_url='login')
def create_comment(request, post_id):
    """This method designed for Ajax calls"""
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.creation_date = datetime.now()
            new_post.post = get_object_or_404(Post, id=post_id)
            new_post.visible = True
            new_post.save()
            return HttpResponse(status=200)
    return HttpResponse(status=403)


@login_required(login_url='login')
def remove_comment(request, comment_id):
    """This method designed for Ajax calls
    System stores deleted messages for security reasons"""
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:
            comment.visible = False
            comment.save()
            return HttpResponse(status=200)
    return HttpResponse(status=403)
