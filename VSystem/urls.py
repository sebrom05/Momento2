"""
URL configuration for VSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp.views import inicio
from persona.views import get_estudiantes, formulario_estudiante,eliminar_estudiante
from curso.views import get_curso, formulario,eliminar_curso
from estudiante_curso.views import Estudiante_Curso, formulario_estudiante_curso,eliminar_estudiante_curso
from matricula.views import lista_matriculas, formulario_matricula,eliminar_matricula



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name= 'inicio'),
    path('Lista-estudiantes/',get_estudiantes, name='lista-estudiantes'),
    path('Lista-cursos/',get_curso,name='lista-cursos'),
    path('cursos/agregar/', formulario, name='formulario_curso'),
    path('estudiantes/agregar/', formulario_estudiante, name='formulario_estudiante'),
     path('estudiantes-curso/', Estudiante_Curso, name='lista-estudiantes-cursos'),  
    path('estudiantes-curso/agregar/', formulario_estudiante_curso, name='formulario_estudiante_curso'),
    path('matriculas/', lista_matriculas, name='lista-matriculas'), 
    path('matriculas/nueva/', formulario_matricula, name='formulario_matricula'),  
    path('eliminar-estudiante/<str:dni>/', eliminar_estudiante, name='eliminar-estudiante'),  
    path('eliminar-estudiante-curso/<int:id>/', eliminar_estudiante_curso, name='eliminar-estudiante-curso'),
    path('eliminar-matricula/<int:id>/', eliminar_matricula, name='eliminar-matricula'),  
    path('eliminar-curso/<int:id>', eliminar_curso, name='eliminar_curso'),


]