from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import StudentForm
from .models import Student

def home(request):
    return HttpResponse("Welcome to the Student Management System!")
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # shows the student list after saving the student
    else:
        form = StudentForm()
    return render(request, 'students/register.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})