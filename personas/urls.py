from django.urls import path
from personas.views import home, personaCreateView, personasAnotherCretateView, personasDeleteView, personasListView, personasShowObject

app_name = 'personas'
urlpatterns = [
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
    path('addPersona', personaCreateView, name="agregarPersona"),
    path('<int:myID>', personasShowObject, name='browsing'),
    path('<int:myID>/delete', personasDeleteView, name='deleting'),
    path('lista/', personasListView, name='listing'),
    path('', home),
]