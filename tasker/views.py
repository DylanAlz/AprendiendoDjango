from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Task

# Create your views here.
def hola(request):
    return render(request, 'index.html')

def Projects(request):
    projects = projects.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def Tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })