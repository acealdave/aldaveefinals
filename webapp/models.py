from django.db import models


class Subject(models.Model):
    TYPE = (
        ('LAB' , 'Laboratory'),
        ('LEC', 'Lecture'),
    )
    subject_code = models.CharField(max_length=50, unique=True, blank=True)
    subject_name = models.CharField(max_length=50, unique=True, blank=True)
    units = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name

class Gender(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('LGBTQ', 'LGBTQ'),
    )
    gender_name = models.CharField(max_length=10, choices=GENDER, unique=True)

    def __str__(self):
        return self.gender_name

class Course(models.Model):
    COURSE = (
        ('IT', 'BSIT'),
        ('CS', 'BSCS'),
    )
    course_name = models.CharField(max_length=10, choices=COURSE, null=True, unique=True)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    studNo = models.IntegerField(unique=True, blank=True)
    email = models.EmailField(max_length=50, unique=True, blank=True)
    age = models.IntegerField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField(Subject, related_name='students', blank=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='schedule', null=True)
    schedule_day = models.CharField(max_length=50, blank=True)
    schedule_time = models.TimeField(null=True, blank=True)
    schedule_end = models.TimeField(null=True, blank=True)
    room = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.schedule_day

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(null=True, blank=True)
    REMARK = (
        ('Passed', 'Passed'),
        ('Conditional', 'Conditional'),
        ('Failed', 'Failed'),
    )
    date_added = models.DateTimeField(auto_now=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    remark = models.CharField(max_length=25, choices=REMARK)

    def __str__(self):
        return f"{self.student.name} - {self.subject.subject_name} - {self.grade} - {self.remark}"

class Professor(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name='professor', blank=True)
    position = models.CharField(max_length=50, blank=True)
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=25, choices=STATUS)

    def __str__(self):
        return self.name

