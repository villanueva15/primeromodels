from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_review/', views.add_review, name='add_review'),
    path('book_reviews/<int:book_id>/', views.book_reviews, name='book_reviews'),
]
