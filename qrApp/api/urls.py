from rest_framework import urlpatterns
from .views import *
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    url(r'^api/alumno/$', AlumnoViewSet.as_view()),
    url(r'^api/buscar_alumno/(?P<id>.+)$', AlumnoBuscarViewSet.as_view()),
    url(r'^api/asistencia/$', AsistenciaViewSet.as_view()),    
    url(r'^api/buscar_asistencia/(?P<id>.+)$', AsistenciaBuscarViewSet.as_view()),
    url(r'^api/profesor/$', ProfesorViewSet.as_view()),
    url(r'^api/buscar_profesor/(?P<id>.+)$', ProfesorBuscarViewSet.as_view()),
    url(r'^api/asignatura/$', AsignaturaViewSet.as_view()),
    url(r'^api/buscar_asignatura/(?P<id>.+)$', AsignaturaBuscarViewSet.as_view()),
    url(r'^api/clase/$', ClaseViewSet.as_view()),
    url(r'^api/buscar_clase/(?P<id>.+)$', ClaseBuscarViewSet.as_view()),
    url(r'^api/curso/$', CursoViewSet.as_view()),
    url(r'^api/buscar_curso/(?P<id>.+)$', CursoBuscarViewSet.as_view()),
    url(r'^api/profesor_api/$', profesorAPI),
    url(r'^api/profesor_api/(?P<id>.+)$', profesorAPI), 
    url(r'^api/asistencia_api/$', asistenciaAPI),
    url(r'^api/asistencia_api/(?P<id>.+)$', asistenciaAPI)

]
urlpatterns = format_suffix_patterns(urlpatterns)
 
