from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import User, Post, Like
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, Http404
from django.core.paginator import Paginator
from django.contrib import messages

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
    # return render(request, 'twitterapp/posts_view.html', {'posts': posts})

    # Paginate the posts
    paginator = Paginator(posts, 5)  # Display 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'twitterapp/posts_view.html', {'page_obj': page_obj})

# Like on posts
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes.add(request.user)  # Add current user to post likes
    updated_likes_count = post.total_likes()
    return HttpResponse(updated_likes_count)

# User profile page with his posts
def user_page(request, username):    
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    # posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-created_at')
    return render(request, 'twitterapp/user_page.html', {'profile_user': profile_user, 'posts': posts})

# Following functionality
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    request.user.following.add(user_to_follow)
    return redirect('user_page', username=username)

# Unfollow functionality
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    request.user.following.remove(user_to_unfollow)
    return redirect('user_page', username=username)

# Show posts os users we follow
def following_users(request):
    if request.user.is_authenticated:
        following_users_ids = request.user.following.values_list('id', flat=True)
        posts = Post.objects.filter(user__in=following_users_ids).order_by('-created_at')
        return render(request, 'twitterapp/following_users.html', {'posts': posts})
    else:
        return render(request, 'twitterapp/login.html')

# Single post view - DOES NOT WORK (page wont render template)
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    print(post.text) # Print to console successful, but does not pass to template.
    return render(request, 'twitterapp/post_detail.html', {'post': post})

# Edit post functionality
@login_required
def edit_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id, user=request.user)    
    except Post.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))
        #raise Http404("Post does not exist or you are not authorized to edit it.")       
    
    print("Post user ID:", post.user.id)
    print("Request user ID:", request.user.id)
    print("Post user:", post.user)
    print("Request user:", request.user)

    if post.user != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        print("Redirecting to index page")
        return HttpResponseRedirect(reverse('index')) # or /
        # return HttpResponseRedirect(reverse("index"))
        #return redirect('posts_view')    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.is_edited = True
            edited_post.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = PostForm(instance=post)
    return render(request, 'twitterapp/edit_post.html', {'form': form, 'post': post})

@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        Like.unlike_post(request.user, post)
        messages.success(request, 'Post unliked successfully.')
    except:
        messages.error(request, "unable to unlike post.")
    updated_likes_count = post.total_likes()
    return HttpResponse(updated_likes_count)