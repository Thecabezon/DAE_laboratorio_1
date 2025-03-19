from django.shortcuts import render
from .models import Classroom

def classroom_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classrooms/classroom_list.html', {'classrooms': classrooms})
