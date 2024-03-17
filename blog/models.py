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
        # One user can create many posts
        # This comment allows the deletion of all posts, if the user entry
        # is deleted then all post will be deleted
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    # created on puts the date and time the blod was posted at
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    # To migrate model to data structure
    # python3 manage.py makemigrations "name of app" --> this wil create migrations folder
    # python3 manage.py migrate "name of app" --> to run the migration

    # META DATA
    # always added after the fields
    # meta class is data about data. This is data that is not a field
    # We can use these classes to add functionailty, even calculate fields
    class Meta:
        ordering = ["-created_on"]

    # We can add methods to Classes
    # These need to be added after meta classes
    def __str__(self):
        # Note the use of f string here to insert text followed by
        # self.title, this will refer to the item number and title
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    # Link te post to the Post model
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        # One user can create many posts
        # This comment allows the deletion of all posts, if the user entry
        # is deleted then all post will be deleted
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
