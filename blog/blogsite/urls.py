from django.urls import path
from . import views
urlpatterns = [
    path('', views.posts, name='posts'),
    path('create_post/', views.create_post, name='create_post'),
    #path('$/', views.posts, name='posts'),
    #path('$/', views.comments, name='comments'),
]
