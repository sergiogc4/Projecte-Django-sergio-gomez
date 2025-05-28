from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('post/', views.post_list, name='post-list'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    path('authors/', views.authors_list, name='authors-list'),
    path('tags/', views.tags_list, name='tags-list'),  # <-- Asegúrate de tener esta ruta
    path('tags/<int:tag_id>/', views.tag_detail, name='tag-detail'),
    path('autor/<int:author_id>/', views.author_detail, name='author-detail'),
]

