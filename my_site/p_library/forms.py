from django import forms
from p_library.models import Author, Book, Friend, Publisher


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Book
        fields = '__all__'


class FriendForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Publisher
        fields = '__all__'