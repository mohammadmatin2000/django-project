from django.urls import path
from blog.views import *
# ======================================================================================================================
app_name = 'blog'
urlpatterns = [
    path('blog/',blog, name='blog'),
    path('<int:pid>',single, name='single'),
    path('base/',base, name='base'),
    path('<str:author_name>',blog, name='author'),
    path('blog/<str:tag_name>',blog, name='tag'),
    path('category/<str:category_name>',blog, name='category'),
]
# ======================================================================================================================