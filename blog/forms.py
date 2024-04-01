from django import forms
from .models import Comment

# We have passed the django forms.ModelForm into the CommentForm
# This is an inbuilt in Django forms
# We then pass a Meta class to tell the forms what we Models and Fields we would like
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)