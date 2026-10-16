from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# 1. READ: Display all students
def home(request):
    students = Student.objects.all().order_by('id')
    form = StudentForm()
    return render(request, 'home.html', {'students': students, 'form': form, 'total_count': students.count()})

# 2. CREATE: Add new student
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student "{student.name}" added successfully!')
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})

# 3. UPDATE: Modify student by ID
def update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student "{student.name}" updated successfully!')
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form': form, 'student': student})

# 4. DELETE: Remove student by ID
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    name = student.name
    student.delete()
    messages.success(request, f'Student "{name}" deleted successfully!')
    return redirect('home')