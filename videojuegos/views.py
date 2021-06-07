from django.shortcuts import render
from videojuegos.models import Videojuego
# Create your views here.
def viewVideojuegos(request, *args, **kwargs):
    videojuegos = Videojuego.objects.all()
    return render(request, "videojuego.html", {"videojuegos":videojuegos})