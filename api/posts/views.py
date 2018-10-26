from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostCreationForm
from datetime import datetime


class CustomPermissionModel(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.author == request.user:
                return True
        return False


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CustomPermissionModel]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = CustomPermissionModel

def index(request):
    posts = Post.objects.all()
    return render(request, './posts/index.html', {'posts': posts})


def details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post, visible=True)
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
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.creation_date = datetime.now()
            new_post.post = get_object_or_404(Post, id=post_id)
            new_post.visible = True
            new_post.save()
    return redirect('details-post', post_id=post_id)

@login_required(login_url='login')
def remove_comment(request, post_id, comment_id):
    """System stores deleted messages for security reasons"""
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:
            comment.visible = False
            comment.save()
    return redirect('details-post', post_id=post_id)