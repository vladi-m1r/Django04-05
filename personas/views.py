from django.shortcuts import render
from personas import forms
from .forms import RawPersonaForm

# Create your views here.
def personasAnotherCretateView(request):
    form = RawPersonaForm()

    context = {
        "form": form,
    }

    return render(request, 'personas/personasCreate.html', context)