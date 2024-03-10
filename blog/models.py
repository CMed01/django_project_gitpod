from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    # Title values should be unique to avoid duplication
    title = models.CharField(max_length=200, unique=True)
    # Slug is a short name for article still under production
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        # One user can create manay posts
        # This comment allows the deletion of all posts, if the user entry
        # is deleted then all post will be deleted
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    # created on puts the date and time the blod was posted at
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)