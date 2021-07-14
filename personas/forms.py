from django import forms
from .models import Persona

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

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'donador',
        ]

    # EL NOMBRE DE LA FUNCION DEBE SER EL MISMO QUE EL CAMPO
    def clean_nombre(self, *args, **kwargs):
        print("Se ejecuto clean_nombre")
        name = self.cleaned_data.get('nombre')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra debe estar en mayuscula')