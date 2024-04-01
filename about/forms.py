from django import forms
from .models import CollaborateRequest

# We have passed the django forms.ModelForm into the CommentForm
# This is an inbuilt in Django forms
# We then pass a Meta class to tell the forms what we Models and Fields we would like
class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name','email','message',)