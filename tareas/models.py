from django.db import models

# Create your models here.
    
class EstadosModelos(models.TextChoices):
    ACTIVO = 'activo', 'Activo'
    INACTIVO = 'inactivo', 'Inactivo'

class TipoPersona(models.TextChoices):
    ESTUDIANTE = 'estudiante', 'Estudiante'
    PROFESOR = 'profesor', 'Profesor'

class Persona(models.Model):
    ci = models.CharField(max_length=7, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    tipo = models.CharField(max_length=15, choices=TipoPersona.choices, default=TipoPersona.ESTUDIANTE)
    estado = models.CharField(max_length=15, choices=EstadosModelos.choices, default=EstadosModelos.ACTIVO)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    estado = models.CharField(max_length=15, choices=EstadosModelos.choices, default=EstadosModelos.ACTIVO)
    profesor = models.ForeignKey('Persona', on_delete=models.CASCADE, related_name='materia_impartida', limit_choices_to={'tipo': TipoPersona.PROFESOR})
    estudiantes = models.ManyToManyField('Persona', related_name='materia_cursada', limit_choices_to={'tipo': TipoPersona.ESTUDIANTE})
    
    def __str__(self):
        return self.nombre

class TareaEstado(models.TextChoices):
    PENDIENTE = 'pendiente', 'Pendiente'
    EN_PROGRESO = 'en_progreso', 'En Progreso'
    COMPLETADA = 'completada', 'Completada'
    CANCELADA = 'cancelada', 'Cancelada'

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    puntaje = models.IntegerField(default=0)
    estado = models.CharField(max_length=15, choices=TareaEstado.choices, default=TareaEstado.PENDIENTE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tarea_asignada', limit_choices_to={'tipo': TipoPersona.ESTUDIANTE})
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='revisa_tarea', limit_choices_to={'tipo': TipoPersona.PROFESOR})

    def __str__(self):
        return self.titulo