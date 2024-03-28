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
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('user/<str:username>/follow/', views.follow_user, name='follow_user'),  # URL for following a user
    path('user/<str:username>/unfollow', views.unfollow_user, name='unfollow_user') # Unfollow
]
