from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from .models import Book, Author, Genre, UserBook


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # make summary and cover_picture optional fields
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


class UserBookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'shelf'
            )
        )

    class Meta:
        model = UserBook
        fields = "__all__"


class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['website'].required = False
        self.fields['twitter_id'].required = False
        self.fields['email_id'].required = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'first_name',
                'last_name',
                'website',
                'twitter_id',
                'email_id',
                'about'
            )
        )

    class Meta:
        model = Author
        fields = "__all__"


class GenreForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'name',
                'description'
            )
        )

    class Meta:
        model = Genre
        fields = "__all__"
