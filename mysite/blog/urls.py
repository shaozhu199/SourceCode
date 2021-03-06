from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name = 'blog_list'),
    path('<blog_pk>', views.blog_detail, name= 'blog_detail'),
    path('type/<blog_type_pk>', views.blogs_with_type, name = 'blogs_with_type'),

]