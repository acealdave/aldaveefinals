from django.shortcuts import render, redirect
from .models import *
from .forms import StudentForm, SubjectForm, ScheduleForm, GradeForm, ProfessorForm


def home(request):
    professor = Professor.objects.all()
    total_professor = professor.count()

    student = Student.objects.all()
    total_student = student.count()

    subject = Subject.objects.all()
    total_subject = subject.count()

    context = {
        'professor':professor,
        'total_professor':total_professor,
        'student':student,
        'total_student':total_student,
         'subject':subject,
        'total_subject':total_subject
    }
    return render(request, 'pages/home.html', context)

def student(request):
    student = Student.objects.all()

    return render(request, 'pages/student.html', {'student': student})

def subject(request):
    subject = Subject.objects.all()
    return render(request, 'pages/subject.html', {'subject': subject})

def schedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'pages/schedule.html', {'schedule': schedule})

def grades(request):
    grade = Grade.objects.all()
    return render(request, 'pages/grades.html', {'grade': grade})

def fees(request):
    return render(request, 'pages/fees.html')

def eval(request):
    return render(request, 'pages/evaluation.html')

def logout(request):
    return render(request, 'pages/logout.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/registration.html')

def addSub(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('subject')
    context = {
        'form':form
    }
    return render(request, 'pages/addSubject.html', context)

def editSub(request, pk):
    subject = Subject.objects.get(id=pk)
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('subject')
    context = {
        'form':form
    }

    return render(request, 'pages/editSubject.html', context)

def deleteSubject(request, pk):
    subject = Subject.objects.get(id=pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('subject')
    context = {
        'subject':subject
    }
    return render(request, 'pages/deleteSubject.html', context)

def addSchedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    context = {
        'form':form
    }
    return render(request, 'pages/addSchedule.html', context)

def editSchedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    form = ScheduleForm(instance=schedule)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('schedule')
    context = {
        'form':form
    }
    return render(request, 'pages/editSchedule.html', context)

def deleteSchedule(request, pk):
    schedule = Schedule.objects.get(id=pk)

    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule')
    context = {
        'schedule':schedule
    }
    return render(request, 'pages/deleteSchedule.html', context)

def addGrade(request):
    form = GradeForm()
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades')

    context = {
        'form':form
    }
    return render(request, 'pages/addGrade.html', context)

def editGrade(request, pk):
    grade = Grade.objects.get(id=pk)
    form = GradeForm(instance=grade)
    context = {
            'form':form
        }

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades')

    return render(request, 'pages/editGrade.html', context)

def deleteGrade(request, pk):
    grade = Grade.objects.get(id=pk)

    if request.method == 'POST':
        grade.delete()
        return redirect('grades')

    context = {
        'grade':grade
    }
    return render(request, 'pages/deleteGrade.html', context)

def addStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {
        'form':form
    }
    return render(request, 'pages/addStudent.html', context)

def editStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student')
    context = {
        'form':form
    }
    return render(request, 'pages/editStudent.html', context)

def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student')
    context = {
        'student':student
    }
    return render(request, 'pages/deleteStudent.html', context)

def addProfessor(request):
    form = ProfessorForm()
    context = {
            'form':form
        }
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'pages/addProfessor.html', context)

def editProfessor(request, pk):
    professor = Professor.objects.get(id=pk)
    form = ProfessorForm(instance=professor)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'pages/editProfessor.html',context)

def deleteProfessor(request, pk):
    professor = Professor.objects.get(id=pk)

    if request.method == 'POST':
        professor.delete()
        return redirect('home')
    context = {
        'professor':professor
    }
    return render(request, 'pages/deleteProfessor.html', context)

