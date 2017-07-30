from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostCreationForm


def index(request):
    posts = Post.objects.all()
    return render(request, './posts/index.html', {'posts': posts})


def details(request, post_id):
    post = get_object_or_404(Post, id=post_id),
    return render(request, './posts/post.html', {'post': post[0]})


@login_required(login_url='login')
def create_post(request):
    form = PostCreationForm()

    if request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            form.instance.author = request.user
            form.save()

            return redirect('home')

    return render(request, './posts/create_post.html', {
        'form': form,
    })