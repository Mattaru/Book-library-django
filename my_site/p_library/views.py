from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.forms import formset_factory

from p_library.models import Book, Publisher, Author, Friend
from p_library.forms import AuthorForm, BookForm, FriendForm, PublisherForm


class HomePage(TemplateView):
    template_name = 'pages/home/home.html'


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'pages/authors/author_create.html'


class AuthorList(ListView):
    model = Author
    template_name = 'pages/authors/author_list.html'


class AuthorUpdate(UpdateView):
    model = Author
    success_url = reverse_lazy('p_library:author_list')
    fields = ['full_name', 'birth_year', 'country']
    template_name = 'pages/authors/author_edit.html'


class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    fields = ['full_name', 'birth_year', 'country']
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'pages/authors/author_delete.html'


class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'pages/friends/friend_create.html'


class FriendList(ListView):
    model = Friend
    template_name = 'pages/friends/friend_list.html'


class FriendUpdate(UpdateView):
    model = Friend
    success_url = reverse_lazy('p_library:friend_list')
    fields = ['full_name', 'birth_year']
    template_name = 'pages/friends/friend_edit.html'


class FriendDelete(DeleteView):
    model = Friend
    form_class = FriendForm
    fields = ['full_name', 'birth_year']
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'pages/friends/friend_delete.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'pages/books/book_create.html'
    success_url = reverse_lazy('p_library:book_list')


class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'pages/books/book_list.html'


class BookUpdate(UpdateView):
    model = Book
    template_name = 'pages/books/book_edit.html'
    fields = ['ISBN', 'title', 'description', 'year_release', 'copy_count', 'book_img', 'price', 'publisher',
              'author', 'reader']
    success_url = reverse_lazy('p_library:book_list')


class BookDelete(DeleteView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:book_list')
    template_name = 'pages/books/book_delete.html'


class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'pages/publishers/publisher_create.html'
    success_url = reverse_lazy('p_library:publisher_list')


class PublisherList(ListView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'pages/publishers/publisher_list.html'


class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['name', 'location', 'owner']
    success_url = reverse_lazy('p_library:publisher_list')
    template_name = 'pages/publishers/publisher_edit.html'


class PublisherDelete(DeleteView):
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('p_library:publisher_list')
    template_name = 'pages/publishers/publisher_delete.html'


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            book.copy_count += 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'pages/authors/manage_authors.html', {
        'author_formset': author_formset
    })


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'pages/authors/manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset
        }
    )