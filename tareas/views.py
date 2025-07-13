from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Persona, Materia, Tarea
from .serializer import PersonaSerializer, MateriaSerializer, TareaSerializer
from rest_framework.decorators import api_view
from .forms import MateriaForm, TareaForm, PersonaForm

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

def materiaFormView(request, id=None):
    form = MateriaForm()
    materia = None
    nombre_en_url = id
    if nombre_en_url:
        materia = get_object_or_404(Materia, id=nombre_en_url)
        form = MateriaForm(instance=materia)

    if request.method == 'POST':
        if materia:
            form = MateriaForm(request.POST, instance=materia if materia else None)

        if form.is_valid():
            form.save()
            return redirect('lista_materias')  # o JsonResponse si querés API

    return render(request, 'editmateria.html', {'form': form})

def tareaFormView(request, id=None):
    form = TareaForm()
    tarea = None
    
    if id:
        tarea = get_object_or_404(Tarea, id=id)
        form = TareaForm(instance=tarea)

    if request.method == 'POST':
        if tarea:
            form = TareaForm(request.POST, instance=tarea if tarea else None)

        if form.is_valid():
            form.save()
            return redirect('lista_tareas')  # o JsonResponse si querés API

    return render(request, 'edittarea.html', {'form': form})

def personaFormView(request, id=None):
    form = PersonaForm()
    persona = None
    nombre_en_url = id
    if nombre_en_url:
        persona = get_object_or_404(Persona, id=nombre_en_url)
        form = PersonaForm(request.POST ,instance=persona if persona else None)

    if request.method == 'POST':
        if persona:
            form = PersonaForm(instance=persona)

        if form.is_valid():
            form.save()
            return redirect('lista_personas')  # o JsonResponse si querés API

    return render(request, 'editpersona.html', {'form': form})

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