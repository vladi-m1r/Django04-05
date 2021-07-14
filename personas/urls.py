from django.urls import path
from personas.views import PersonaDetailView, PersonaListView, home, personaCreateView, personasAnotherCretateView, personasDeleteView, personasListView, personasShowObject


app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name= 'persona-list'),
    path('<int:pk>', PersonaDetailView.as_view(), name= 'persona-detail'),
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
    path('addPersona', personaCreateView, name="agregarPersona"),
    path('<int:myID>/delete', personasDeleteView, name='deleting'),
    path('lista/', personasListView, name='listing'),
]