from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.app.books'
    verbose_name = '書籍'
    verbose_name_plural = '書籍'
