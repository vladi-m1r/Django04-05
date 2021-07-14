from django.urls import path
from personas.views import personaCreateView, personasAnotherCretateView

urlpatterns = [
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
    path('addPersona', personaCreateView, name="agregarPersona"),
]