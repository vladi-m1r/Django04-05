from django import forms

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder': "Solo tu nombre, porfavor",
                'id': 'nombreID',
                'class': 'special',
                'cols': '10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 20)
    donador = forms.BooleanField()