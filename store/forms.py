from django import forms
from .models import Books,Store

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        
class StoreForm(forms.ModelForm):
    # customer = forms.CharField(disabled = True,required=False,)
    class Meta:
        model = Store
        fields = ['store_name', 'owner_name','book_name','store_image',]
        exclude=['customer']