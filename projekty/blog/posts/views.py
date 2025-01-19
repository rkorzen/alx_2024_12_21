from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

@login_required
def posts_list(request):
    posts = Post.objects.filter(status="published")
    return render(request, "posts/list.html", {"posts": posts})

@login_required
def post_details(request, post_id):
    form = None
    post = get_object_or_404(Post, id=post_id, status="published")
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        
    
    if request.user == post.author:
        form = PostForm(instance=post)
        
    
    # post = Post.objects.get(id=post_id, status="published")
    return render(request, "posts/details.html", {"post": post, "form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
        
    return render(request, "posts/login.html", {"form": form})