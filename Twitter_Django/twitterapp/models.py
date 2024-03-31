from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    def following_count(self):
        return self.following.count()

# Create post module
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_posts', blank=True)
    is_edited = models.BooleanField(default=False)  # Add a field to track if the post has been edited
    edited_text = models.TextField(blank=True, null=True)  # Field to store the edited content
    def __str__(self):
        return f'Posted by: {self.user.username} on {self.created_at}'
    def total_likes(self):
        return self.likes.count()
    
# Likes on posts
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'post')  # Ensure each user can like a post only once
    # Unlike
    @classmethod
    def unlike_post(cls, user, post):
        try:
            like = cls.objects.get(user=user, post=post)
            like.delete()
            return True  # Return True if unlike is successful
        except cls.DoesNotExist:
            return False  # Return False if like does not exist