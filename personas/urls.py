from django.urls import path
from personas.views import personaCreateView, personasAnotherCretateView, personasDeleteView, personasShowObject

urlpatterns = [
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
    path('addPersona', personaCreateView, name="agregarPersona"),
    path('<int:myID>', personasShowObject, name='browsing'),
    path('<int:myID>/delete', personasDeleteView, name='deleting'),
]