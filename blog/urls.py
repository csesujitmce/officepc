from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list_view, name="blog"),
    path('<str:slug>', views.blog_details_view, name="blog_details"),
]

