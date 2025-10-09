from django import forms
from .models import BuyedBooks

class BuyedBooksForm(forms.ModelForm):
    class Meta:
        model = BuyedBooks
        fields = '__all__'
