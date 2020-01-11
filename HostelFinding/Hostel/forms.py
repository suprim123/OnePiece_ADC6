from django import forms
from .models import Hostel
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = '__all__'