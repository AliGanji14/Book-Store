from django.contrib import admin

from .models import Book, Comment


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ("title", "author", "price",)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ("user", "book", "text", "datetime_created", "recommend", "is_active",)
