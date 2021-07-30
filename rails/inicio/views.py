from django.shortcuts import render

# Create your views here.
def viewHome(request, *args, **kwargs):
    return render(request, "home.html", {})