from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import User, Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db.models import Count
import logging

def index(request):
    return render(request, "twitterapp/posts_view.html")

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "twitterapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "twitterapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "twitterapp/register.html", {
                "message": "Passwords must match."
            })
        is_admin = request.POST.get("is_admin")  # Check if "is_admin" checkbox is checked
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            if is_admin:
                user.is_admin = True
            user.save()
        except IntegrityError:
            return render(request, "twitterapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "twitterapp/register.html")

# Create post
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "twitterapp/create_post.html", {'form': form, 'posts': posts})

# View posts page
def posts_view(request):
    posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-created_at')
    return render(request, 'twitterapp/posts_view.html', {'posts': posts})

# Like on posts
def like_post(request, post_id):
    # Get post object or return 404
    # post = get_object_or_404(Post, pk=post_id)
    # post.likes.add(request.user) # Add current user to post likes
    # posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-created_at')
    # # return redirect('posts_view')
    # return render(request, 'twitterapp/posts_view.html', {'posts': posts})
    post = get_object_or_404(Post, pk=post_id)
    # Process the like action...
    post.likes.add(request.user)  # Add current user to post likes
    # Get the updated like count for the post
    updated_likes_count = post.total_likes()
    # Return the updated like count as plain text
    return HttpResponse(updated_likes_count)
