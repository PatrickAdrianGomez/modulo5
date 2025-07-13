from django.core.exceptions import ValidationError
from django.utils import timezone
import re

def validar_fecha_vencimiento(value):
    if value < timezone.now():
        raise ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")

def validar_puntaje(value):
    if value < 0:
        raise ValidationError("El puntaje no puede ser negativo.")
    if value > 100:
        raise ValidationError("El puntaje no puede ser mayor a 100.")
    
def validar_textos(value):
    if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', value):
        raise ValidationError("El campo solo puede contener letras y espacios.")
    if len(value.strip()) < 3:
        raise ValidationError("El campo debe tener al menos 3 caracteres.")

def validar_tipo_persona(value, tipo_esperado):
    if value.tipo != tipo_esperado:
        raise ValidationError(f"El campo debe ser un {tipo_esperado}.")

# def validar_estudiante_registrado(value):
#     if not Persona.objects.filter(ci=value.ci, tipo='estudiante').exists():
#         raise ValidationError("El estudiante no está registrado.")
#     
# def validar_profesor_registrado(value):
#     if not Persona.objects.filter(ci=value.ci, tipo='profesor').exists():
#         raise ValidationError("El profesor no está registrado.")