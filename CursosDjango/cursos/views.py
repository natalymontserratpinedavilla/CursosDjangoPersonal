from django.shortcuts import render
from .models import Cursos

def lista_cursos(request):  # nombre más claro
    cursos = Cursos.objects.all()
    return render(request, "cursos/principal.html", {'cursos': cursos})
