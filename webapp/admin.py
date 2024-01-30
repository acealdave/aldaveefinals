from django.contrib import admin
from .models import Student, Course, Gender, Grade, Subject, Schedule, Professor

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Gender)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Professor)

