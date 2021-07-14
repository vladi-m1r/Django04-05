from django.shortcuts import get_object_or_404, redirect, render
from personas import forms
from personas.models import Persona
from .forms import RawPersonaForm, PersonaForm

def personasListView(request):

    querySet = Persona.objects.all()
    context = {
        'objectList': querySet,
    }

    return render(request, 'personasLista.html', context)


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

    initialValues = {
        'nombre' : 'Sin nombre',
    }

    form = PersonaForm(request.POST or None, initial = initialValues)

    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form': form,
    }

    return render(request, 'personasCreate.html', context)

# RUTEO DINAMICO
def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    context = {
        'objeto': obj,
    }
    return render(request, 'descripcion.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == "POST":
        print("Lo borro")
        obj.delete()
        return redirect("../")
    context = {
        'objeto': obj,
    }

    return render(request, 'personasDelete.html', context)

def home(request):
    return render(request, 'base.html')