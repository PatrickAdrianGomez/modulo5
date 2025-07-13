from django.contrib import admin
from .models import Persona, Materia, Tarea

# Register your models here.
# admin.site.register(Persona)
# admin.site.register(Materia)
# admin.site.register(Tarea) 

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('ci', 'nombre', 'apellido', 'email', 'fecha_nacimiento', 'tipo', 'estado')
    search_fields = ('ci', 'nombre', 'apellido', 'email', 'tipo', 'estado')
    ordering = ('apellido', 'nombre')
    filter_fileds = ('tipo', 'estado')
    list_filter = ('tipo', 'estado')
admin.site.register(Persona, PersonaAdmin)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'creditos', 'estado', 'profesor')
    search_fields = ('nombre', 'descripcion', 'profesor__nombre', 'profesor__apellido')
    ordering = ('nombre',)
    filter_fileds = ('estado',)
    list_filter = ('estado',)
    filter_horizontal = ('estudiantes',)
    autocomplete_fields = ('profesor',)
admin.site.register(Materia, MateriaAdmin)

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_creacion', 'fecha_vencimiento', 'puntaje', 'estado', 'materia', 'estudiante', 'profesor')
    search_fields = ('titulo', 'descripcion', 'materia__nombre', 'estudiante__nombre', 'profesor__nombre')
    ordering = ('fecha_creacion','fecha_vencimiento')
    filter_fileds = ('estado',)
    list_filter = ('estado', 'materia')
    autocomplete_fields = ('materia', 'estudiante', 'profesor')
admin.site.register(Tarea, TareaAdmin)