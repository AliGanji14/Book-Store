from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import CommentForm, BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"
    context_object_name = "books"


@login_required
def book_detail_view(request, pk):
    # get object book
    book = get_object_or_404(Book, pk=pk)
    # get book comment
    book_comment = book.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, "books/book_detail.html", {
        "book": book,
        "comments": book_comment,
        "comment_form": comment_form,
    })


def book_create_view(request):
    if request.method == "POST":
        create_book = BookForm(request.POST)
        if create_book.is_valid():
            new_book = create_book.save(commit=False)
            new_book.user = request.user
            new_book.save()
            return redirect(new_book)

    else:
        create_book = BookForm()

    return render(request, "books/book_create.html", {
        "form_book": create_book
    })


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    model = Book
    fields = ["title", "author", "description", "price", "cover"]
    template_name = "books/book_update.html"


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")
