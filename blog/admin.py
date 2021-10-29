from django.contrib import admin
from .models import Category,BlogPost
from django_summernote.admin import SummernoteModelAdmin
   
    
class PostAdminSummer(SummernoteModelAdmin):
    model = BlogPost
    summernote_fields = ('description', )
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category)
admin.site.register(BlogPost,PostAdminSummer)