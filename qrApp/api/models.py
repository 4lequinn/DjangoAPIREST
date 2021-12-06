from django.db import models
from datetime import datetime, date

# Create your models here.

## Considerar usar el AUTOFIELD

class Curso(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    seccion = models.CharField(max_length=50)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE,related_name='+',blank=True)
    def __str__(self):
        return self.id  

class Clase(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    hora = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    #hora = models.DateTimeField(auto_now_add=True, blank=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE,related_name='+',null=False,blank=True)
    def __str__(self):
        return self.id

class Asignatura(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    curso = models.ManyToManyField('Curso',related_name='+',blank=True)
   # presente = models.BooleanField()
    def __str__(self):
        return self.id

class Alumno(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    asignatura = models.ManyToManyField(Asignatura)
    def __str__(self):
        return self.id

class Profesor(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    curso = models.ManyToManyField('Curso',related_name='curso',blank=True)
    def __str__(self):
        return self.id        

class Asistencia(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    presente = models.BooleanField()
    def __str__(self):
        return str(self.id)






    
