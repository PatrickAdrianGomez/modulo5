from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'personas', views.PersonaViewSet)
router.register(r'tareas', views.TareaViewSet)
router.register(r'materias', views.MateriaViewSet)

urlpatterns = [
    path('', views.index, name='index'),  # Home page for the tareas app
    path('personas/', views.lista_personas, name='lista_personas'),  # List of personas
    path('materias/', views.lista_materias, name='lista_materias'),  # List of materias
    path('tareas/', views.lista_tareas, name='lista_tareas'),  # List of tareas
    path('tareas/<int:id>/', views.lista_tareas, name='detalle_tarea'),  # Detail view for a specific tarea
    path('materias/<int:id>/', views.lista_materias, name='detalle_materia'),  # Detail view for a specific materia
    path('personas/<int:id>/', views.lista_personas, name='detalle_persona'),  # Detail view for a specific persona
    path('materias/cantidad/', views.materia_count, name='materia-count'),
    path('personas/estudiantes/', views.alumnos_count, name='alumnos-count'),
    path('personas_editar/<int:id>/', views.personaFormView, name='editar_persona'),  # Edit view for a specific persona
    path('materias_editar/<int:id>/', views.materiaFormView, name='editar_materia'),  # Edit view for a specific materia
    path('tareas_editar/<int:id>/', views.tareaFormView, name='editar_tarea'),  # Edit view for a specific tarea

    path('crud/', include(router.urls)),
]