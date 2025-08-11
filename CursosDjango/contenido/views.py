from django.shortcuts import render, HttpResponse


def contacto(request):
  
    return render(request,"contenido/contacto.html")

def cursos(request):
   
    return render(request,"contenido/cursos.html")

def principal(request):
    
    return render(request,"contenido/principal.html")
