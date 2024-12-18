from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    author = models.CharField(max_length=255, verbose_name="Autor")
    published_date = models.DateField(verbose_name="Fecha de publicación")
    genre = models.CharField(max_length=100, default="General", verbose_name="Género")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews", verbose_name="Libro")
    user = models.CharField(max_length=255, verbose_name="Usuario")
    comment = models.TextField(verbose_name="Comentario")
    rating = models.PositiveIntegerField(verbose_name="Calificación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f"Reseña de {self.book.title} por {self.user}"
