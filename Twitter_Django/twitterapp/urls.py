from django.urls import path
from . import views
from .views import create_post

urlpatterns = [
    path("", views.posts_view, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    # path('posts/', views.posts_view, name='posts_view'),
    path('user/<str:username>/', views.user_page, name='user_page')
]
