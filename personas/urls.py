from django.urls import path
from personas.views import personasAnotherCretateView

urlpatterns = [
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
]