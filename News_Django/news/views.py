from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User
from django.contrib.auth.hashers import check_password # For hash pass check
import requests
from bs4 import BeautifulSoup

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
            #return HttpResponseRedirect(reverse("choose_news"))
            return render(request, "news/index.html")
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
    
def extract_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all elements with class 'card__article-link'
        titles = soup.find_all(class_='card__title')
        # Extract the titles from the elements
        title_list = [title.get_text() for title in titles]
        return title_list
    else:
        print('Error fetching webpage:', response.status_code)
        return []

def choose_news(request):    
    url = 'https://www.jutarnji.hr/vijesti/najcitanije'
    titles = extract_title(url)
    url2 = 'https://www.jutarnji.hr/vijesti/najnovije'
    titles2 = extract_title(url2)
    zipped_titles = zip(titles, titles2)
    return render(request, "news/choose_news.html", {'user': request.user, 'zipped_titles': zipped_titles })

def extract_vecernji(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        component_light = soup.find(class_='component--light')

        # Check if the component has the href attribute and its value is '#najnovije'
        if component_light and component_light.find('a', href='#najcitanije'):
            # Find all h3 elements within the component
            h3_titles = component_light.find_all('h3')
            # Extract text from each h3 element and store it in a list
            titles_list = [h3.get_text(strip=True) for h3 in h3_titles]
            # Return the list of titles
            return titles_list
        else:
            # Return None or handle the case where the component or the href attribute is not found
            return None

        # component_light = soup.find(class_='component--light')
        # h3_titles = component_light.find_all('h3')
        # titles_list = [h3.get_text(strip=True) for h3 in h3_titles]
        # return titles_list

        # h3_tags = soup.find_all(class_='card__title')
        # titles = [tag.get_text(strip=True) for tag in h3_tags]
        # return titles
    else:
        print('Error fetching webpage:', response.status_code)
        return []

def vecernji(request):
    vec = 'https://www.vecernji.hr/'
    vectitles = extract_vecernji(vec)
    # vec2 = 'https://www.vecernji.hr/'
    # vectitles2 = extract_vecernji(vec2)
    # zipped_titles = zip(vectitles, vectitles2)
    return render(request, "news/vecernji.html", {'user': request.user, 'vectitles': vectitles })