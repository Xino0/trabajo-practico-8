from django.shortcuts import render, get_object_or_404
from apps.estudiante.models import Estudiante, Curso

# Vista para mostrar todos los estudiantes y sus cursos
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.select_related('curso').all()
    return render(request, 'estudiante/lista_estudiantes.html', {'estudiantes': estudiantes})

# Vista para mostrar estudiantes mayores de una edad específica
def estudiantes_mayores_de(request, edad):
    estudiantes = Estudiante.objects.filter(edad__gt=edad)
    return render(request, 'estudiante/estudiantes_mayores_de.html', {'estudiantes': estudiantes, 'edad': edad})

# Vista para mostrar los detalles de un curso específico
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiantes = Estudiante.objects.filter(curso=curso)
    return render(request, 'estudiante/detalle_curso.html', {'curso': curso, 'estudiantes': estudiantes})
