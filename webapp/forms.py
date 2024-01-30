from django.forms import ModelForm
from .models import Student, Subject, Schedule, Grade, Professor

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
