from django import forms

class RawPersonaForm(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()