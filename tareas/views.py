from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Persona, Materia, Tarea
from .serializer import PersonaSerializer, MateriaSerializer, TareaSerializer
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return HttpResponse("¡Bienvenidoa a la aplicación de Tareas!")

def lista_personas(request):
    nombre_en_url = request.GET.get('id')
    if nombre_en_url:
        personas = get_object_or_404(Persona, id=nombre_en_url)
        personas = Persona.objects.filter(id=nombre_en_url)
    else:
        personas = Persona.objects.all()
    return render(request, 'usuarios.html', {'personas': personas})

def lista_materias(request):
    nombre_en_url = request.GET.get('id')
    if nombre_en_url:
        materias = get_object_or_404(Materia, id=nombre_en_url)
        materias = Materia.objects.filter(id=nombre_en_url)
    else:
        materias = Materia.objects.all()
    return render(request, 'materias.html', {'materias': materias})

def lista_tareas(request):
    nombre_en_url = request.GET.get('id')
    if nombre_en_url:
        tareas = get_object_or_404(Tarea, id=nombre_en_url)
        tareas = Tarea.objects.filter(id=nombre_en_url)
    else:
        tareas = Tarea.objects.all()
    return render(request, 'tareas.html', {'tareas': tareas})

@api_view(['GET'])
def materia_count(request):
    try:
        cantidad = Materia.objects.count()
        return JsonResponse({
            'cantidad': cantidad
        },
        safe= False,
        status= 200
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status= 400)
    
@api_view(['GET'])
def alumnos_count(request):
    try:
        alumnos = Persona.objects.filter(tipo='estudiante')
        return JsonResponse(
            PersonaSerializer(alumnos, many=True).data,
            safe= False,
            status= 200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status= 400)

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer