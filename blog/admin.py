from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # This display the fields on the table
    list_display = ('title', 'slug', 'status', 'created_on')
    # This allows the user to search for content in the desired fields - i.e title
    # This speeds up the searching
    search_fields = ['title','content']
    # This provides the filters to be applied. I.e. by author or status (publihsed or draft)
    list_filter = ('status','created_on',)
    # This function now automatically creates the slug
    # slug then the field to be created into a slug
    prepopulated_fields = {'slug': ('title',)}
    # this add the rish text editor to the field that is passed.
    summernote_fields = ('content',)

# Register your models here.

# This will allow you to create, update and delete blog posts from the admin panel. 
# However, please refrain from adding any posts at the moment, 
# as there are more fields to be added to the tables in an upcoming topic.
admin.site.register(Comment)