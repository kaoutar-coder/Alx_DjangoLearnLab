
from django import ExampleForm

class BookSearchForm(ExampleForm.Form):
    q = ExampleForm.CharField(label='Search', max_length=100, required=False)

    