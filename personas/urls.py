from django.urls import path
from personas.views import PersonaCreateView, PersonaDeleteView, PersonaDetailView, PersonaListView, PersonaQueryView, PersonaUpdateView, home, personaCreateView, personasAnotherCretateView, personasDeleteView, personasListView, personasShowObject


app_name = 'personas'
urlpatterns = [
    path('query/', PersonaQueryView.as_view(), name= 'persona-query' ),
    path('<int:pk>/delete', PersonaDeleteView.as_view(), name= 'persona-delete'),
    path('<int:pk>/update', PersonaUpdateView.as_view(), name= 'persona-update'),
    path('create/', PersonaCreateView.as_view(), name= 'persona-create'),
    path('', PersonaListView.as_view(), name= 'persona-list'),
    path('<int:pk>', PersonaDetailView.as_view(), name= 'persona-detail'),
    path('anotherAdd', personasAnotherCretateView, name="OtroAgregarPersonas"),
    path('addPersona', personaCreateView, name="agregarPersona"),
    path('<int:myID>/delete', personasDeleteView, name='deleting'),
    path('lista/', personasListView, name='listing'),
]