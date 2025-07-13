from rest_framework import serializers
from .models import Tarea, Persona, Materia

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'