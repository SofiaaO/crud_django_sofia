from django import forms
from .models import *

class AutorForm (forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'