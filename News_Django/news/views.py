from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password # For hash pass check

# Create your views here.
def index(request):
    return render(request, "news/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)

        # Checn pass vs hashed pass
        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     print("User does not exist")
        # if user:
        #     hashed_password = user.password
        # if check_password(password, hashed_password):
        #     print("Password match")
        # else:
        #     print("Password does not match")

        # Attempt to authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("Authenticated user:", user)
            return HttpResponseRedirect(reverse("choose_news"))
        else:
            return render(request, "news/login.html", {
                "message": "Invalid username and/or password."
            })

        # Check if authentication successful
    else:
        return render(request, "news/login.html")

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
            return render(request, "news/register.html", {
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
            return render(request, "news/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "news/register.html")
    
def choose_news(request):    
    return render(request, "news/choose_news.html")