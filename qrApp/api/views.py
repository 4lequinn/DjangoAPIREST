from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db import connection
from .models import *
from .serializers import *
from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


#Viewsets del alumno
class AlumnoViewSet(generics.ListAPIView): # Lista de un Alumno
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoBuscarViewSet(generics.ListAPIView): # Lista de todos los Alumnos
    serializer_class = AlumnoSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Alumno.objects.filter(id=laid)
#Viewsets del alumno

#Viewsets del profesor
class ProfesorViewSet(generics.ListAPIView): # Lista de todos los Profesores
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.all()

class ProfesorBuscarViewSet(generics.ListAPIView): # Lista de un Profesor
    serializer_class = ProfesorSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Profesor.objects.filter(id=laid)


#Viewsets del profesor

#Viewsets del curso
class CursoViewSet(generics.ListAPIView): # Lista de todos los Cursos
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class CursoBuscarViewSet(generics.ListAPIView): # Lista de un Curso
    serializer_class = CursoSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Curso.objects.filter(id=laid)
#Viewsets del curso

#Viewsets de la asistencia
class AsistenciaViewSet(generics.ListAPIView): # Lista de todas las Asistencias
    serializer_class = AsistenciaSerializer
    queryset = Asistencia.objects.all()

class AsistenciaBuscarViewSet(generics.ListAPIView): # Lista de una Asistencia
    serializer_class = AsistenciaSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Asistencia.objects.filter(id=laid)
#Viewsets de la asistencia

#Viewsets de la Asignatura
class AsignaturaViewSet(generics.ListAPIView): # Lista de todas las Asignaturas
    serializer_class = AsignaturaSerializer
    queryset = Asignatura.objects.all()

class AsignaturaBuscarViewSet(generics.ListAPIView): # Lista de una Asignatura
    serializer_class = AsignaturaSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Asignatura.objects.filter(id=laid)
#Viewsets de la Asignatura

#Viewsets de la Clase
class ClaseViewSet(generics.ListAPIView): # Lista de todas las Clases
    serializer_class = ClaseSerializer
    queryset = Clase.objects.all()

class ClaseBuscarViewSet(generics.ListAPIView): # Lista de una Clase
    serializer_class = ClaseSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Clase.objects.filter(id=laid)
#Viewsets de la Clase

#Viewsets de la Curso
class CursoViewSet(generics.ListAPIView): # Lista de todos los Cursos
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class CursoBuscarViewSet(generics.ListAPIView): # Lista de un Curso
    serializer_class = CursoSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Curso.objects.filter(id=laid)
#Viewsets de la Curso

@csrf_exempt
def profesorAPI(request,id=0):
    if request.method=='GET':
        profesores = Profesor.objects.all()
        profesores_serializers = ProfesorSerializer(profesores, many=True)
        return JsonResponse(profesores_serializers.data, safe=False)
    if request.method=='POST':
        profesor_data = JSONParser().parse(request)
        profesor_serializers = ProfesorSerializer(data=profesor_data)
        if profesor_serializers.is_valid():
            profesor_serializers.save()
            return JsonResponse("Profesor agregado correctamente.",safe=False)
        return JsonResponse("No se pudo agregar un Profesor",safe=False)


@csrf_exempt
def asistenciaAPI(request,id=0):
    if request.method=='GET':
        asistencia = Asistencia.objects.all()
        asistencia_serializer = AsistenciaSerializer(asistencia,many=True)
        return JsonResponse(asistencia_serializer.data,safe=False)
    if request.method=='POST':
        asistencia_data = JSONParser().parse(request)
        asistencia_serializer = AsistenciaSerializer(data=asistencia_data)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return JsonResponse("AGREGADA",safe=False)
        return JsonResponse("NO PUDO AGREGAR",safe=False)
    if request.method=='DELETE':
        try:
            asistencia = Asistencia.objects.get(id=id)
            asistencia.delete()
            return JsonResponse("ELIMINADO",safe=False) 
        except :
            return JsonResponse("NO PUDO ELIMINAR",safe=False)
    if request.method=='PUT':
        asistencia_data=JSONParser().parse(request)
        asistencia = Asistencia.objects.get(id= asistencia_data['id'])
        asistencia_serializer = AsistenciaSerializer(asistencia,data=asistencia_data)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return JsonResponse('Actualizo',safe=False)
        return JsonResponse('No pudo Actualizar',safe =False)

@csrf_exempt
def conteo_asistencias(request):
    if request.method=='POST':        
        cantidad = Asistencia.objects.all().count()
        return JsonResponse(cantidad,safe=False)
    return JsonResponse(0,safe=False)        