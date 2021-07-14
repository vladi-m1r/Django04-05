from django.shortcuts import render
from personas import forms
from .forms import RawPersonaForm

# Create your views here.
def personasAnotherCretateView(request):
    form = RawPersonaForm()

    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)

    context = {
        "form": form,
    }

    return render(request, 'personasCreate.html', context)