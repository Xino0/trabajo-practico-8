from django.urls import path
from apps.estudiante import views

urlpatterns = [
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/mayores_de/<int:edad>/', views.estudiantes_mayores_de, name='estudiantes_mayores_de'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]
