from django.urls import path
from personas.views import PersonaListView, home, personaCreateView, personasAnotherCretateView, personasDeleteView, personasListView, personasShowObject


app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name= 'persona-list'),
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
    path('addPersona', personaCreateView, name="agregarPersona"),
    path('<int:myID>', personasShowObject, name='browsing'),
    path('<int:myID>/delete', personasDeleteView, name='deleting'),
    path('lista/', personasListView, name='listing'),
]