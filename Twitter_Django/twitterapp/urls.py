from django.urls import path
from . import views
from .views import create_post

urlpatterns = [
    path("", views.posts_view, name="index"),
    # path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('user/<str:username>/follow/', views.follow_user, name='follow_user'),  # URL for following a user
    path('user/<str:username>/unfollow', views.unfollow_user, name='unfollow_user'), # Unfollow
    path('following_users', views.following_users, name='following_users'), # See posts of users we follow
    # path('get_paginated_posts', views.get_paginated_posts, name='get_paginated_posts'), # Pagination
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('unlike/<int:post_id>/', views.unlike_post, name='unlike_post'),
]
