from django.urls import path,include
from .views import BlogListView,BlogDetailview,CategoryView
urlpatterns = [
    path('',BlogListView.as_view()),
    path('<slug:slug>/',BlogDetailview.as_view()),
    # Handle the category --> post like a charm
    path('category/<str:categoriesvalue>/<slug:slug>/',BlogDetailview.as_view()),
    # <Path converter: url input>
    path('category/<str:categoriesvalue>/',CategoryView,name='categoriesvalue')
]
