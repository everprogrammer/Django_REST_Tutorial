from django.contrib import admin
from django.urls import path
from ns_app import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view()),
    path('authors/<int:pk>', views.AuthorDetailView.as_view()),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>', views.BookDetailView.as_view()),
]
