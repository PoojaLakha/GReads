from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from .models import Book, Author, Genre


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # make description optional field
        self.fields['summary'].required = False
        self.fields['cover_picture'].required = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'isbn',
                'title',
                'author',
                'genre',
                'summary',
                'cover_picture'
            )
        )

    class Meta:
        model = Book
        fields = "__all__"


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
