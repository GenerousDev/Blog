from typing import List
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import BlogPost,Category

# Create your views here.

class BlogListView(ListView):
    model = BlogPost
    context_object_name ='blog_list'
    template_name = 'blog_list.html'
    def get_context_data(self, **kwargs):
        context  = super(BlogListView,self).get_context_data(**kwargs)
        context['category'] = Category.objects.order_by('title')
        return context

class BlogDetailview(DetailView):
    model = BlogPost
    context_object_name = 'blog_detail'
    template_name ='blog_detail.html'

def CategoryView(request,categoriesvalue):
    blogcategory = BlogPost.objects.filter(categories__title = categoriesvalue)
    print(blogcategory)
    return render(request,'category.html',{'categoriesvalue':blogcategory})
    