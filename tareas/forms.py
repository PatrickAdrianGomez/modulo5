from django import forms
from .models import Materia, Persona, Tarea

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"