from django.forms import ModelForm
from .models import BookDB


class BookForm(ModelForm):

    class Meta:
        model = BookDB
        fields = '__all__'

class BookUpdateForm(ModelForm):
    
    class Meta:
        model = BookDB
        fields = '__all__'