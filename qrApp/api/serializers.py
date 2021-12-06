from .models import *
from rest_framework import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ["id","usuario","password","asignatura"]

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id","alumno","profesor","fecha","hora","clase","presente"]

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ["id","usuario","password","curso"]

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ["id","nombre","curso"]

class ClaseSerializer(serializers.ModelSerializer):
    hora = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Clase
        fields = ["id","hora","curso"]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["id","seccion","asignatura"]
        
