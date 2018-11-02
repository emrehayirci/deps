from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework import permissions, status
from .serializers import PostSerializer, CommentSerializer, UpVoteSerializer, DownVoteSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse
from .models import Post, Comment, UpVote, DownVote
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

    def create(self, request,  *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            Post.objects.create(**serializer.validated_data, author=request.user, creation_date=datetime.now())

            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    #Update with filtering
    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class CommentViewSet(GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermissionModel]

    def create(self, request,  *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Comment.objects.create(**serializer.validated_data, author=request.user, creation_date=datetime.now())
            print(serializer.validated_data)
            return Response(
                status=status.HTTP_201_CREATED
            )

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

"""
ALl of the views below is deprecated and will be removed as soon as new SPA Client ready!
"""


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