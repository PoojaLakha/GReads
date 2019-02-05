from django.forms import ModelForm
from django import forms
from .models import Book, Author, Genre


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
    # authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    # genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"


def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['authors'] = [a.pk for a in kwargs['instance'].
                                  author_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)


# Overriding save
def save(self, commit=True):
        # Get the unsave instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            instance.author_set.clear()
            instance.author_set.add(*self.cleaned_data['authors'])
        self.save_m2m = save_m2m

        instance.save()
        self.save_m2m()

        return instance
