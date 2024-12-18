from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book
from .forms import BookForm, ReviewForm
from django.shortcuts import get_object_or_404

def book_list(request):
    books = Book.objects.all()
    book_form = BookForm()
    review_form = ReviewForm()
    return render(request, 'reviews/book_list.html', {
        'books': books,
        'book_form': book_form,
        'review_form': review_form,
    })

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors})
def book_reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    reviews_data = [
        {
            "user": review.user,
            "comment": review.comment,
            "rating": review.rating,
            "created_at": review.created_at.strftime("%d/%m/%Y %H:%M"),
        }
        for review in reviews
    ]
    return JsonResponse({"book_title": book.title, "reviews": reviews_data})
