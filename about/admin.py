from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)

class AboutAdmin(SummernoteModelAdmin):
    # This display the fields on the table
    # list_display = ('title', 'content', 'updated_on')
    # # This allows the user to search for content in the desired fields - i.e title
    # # This speeds up the searching
    # # search_fields = ['title','content']
    # # # This provides the filters to be applied. I.e. by author or status (publihsed or draft)
    # # list_filter = ('status','created_on',)
    # # # This function now automatically creates the slug
    # # # slug then the field to be created into a slug
    # # prepopulated_fields = {'slug': ('title',)}
    # # this add the rish text editor to the field that is passed.
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)