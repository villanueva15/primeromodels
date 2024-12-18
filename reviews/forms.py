from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'published_date': 'Fecha de publicación',
            'genre': 'Género',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'user', 'comment', 'rating']
        labels = {
            'book': 'Libro',
            'user': 'Usuario',
            'comment': 'Comentario',
            'rating': 'Calificación',
        }
