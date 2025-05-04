from django import forms

class TemaForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=200)
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')
    autor = forms.CharField(label='Autor', max_length=100)
