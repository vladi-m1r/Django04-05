from django.shortcuts import render
from personas import forms
from personas.models import Persona
from .forms import RawPersonaForm, PersonaForm

# Create your views here.
def personasAnotherCretateView(request):
    form = RawPersonaForm()

    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context = {
        "form": form,
    }

    return render(request, 'personasCreate.html', context)

def personaCreateView(request):
    
    obj = Persona.objects.get(id = 2)
    form = PersonaForm(request.POST or None, instance = obj)
    
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form': form
    }

    return render(request, 'personasCreate.html', context)
