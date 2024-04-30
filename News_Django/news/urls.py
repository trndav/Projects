from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("choose_news/", views.choose_news, name="choose_news"),
    path("vecernji/", views.vecernji, name="vecernji"),
    path("24sata/", views.sata24, name="sata24"),
    path("users/", views.users, name="users"),
]
