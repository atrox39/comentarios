from django import forms
from django.forms import ModelForm, HiddenInput, Textarea
from .models import *

class CrearComentario(ModelForm):
    contenido = forms.CharField(widget=Textarea(attrs={'class':'form-control', 'rows':3}))
    class Meta:
        model = Comentario
        fields = ['usuario', 'publicacion', 'contenido']