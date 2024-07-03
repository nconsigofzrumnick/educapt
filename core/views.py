from django.shortcuts import render
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'content/lista_cursos.html', {'cursos': cursos})

def detalhe_curso(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'content/detalhe_curso.html', {'curso': curso})
