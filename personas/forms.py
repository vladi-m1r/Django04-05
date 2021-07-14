from django import forms

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(label = "Tu nombre")
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 20)
    donador = forms.BooleanField()