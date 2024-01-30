from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('student/', views.student, name="student"),
    path('subject/', views.subject, name="subject"),
    path('schedule/', views.schedule, name="schedule"),
    path('grades/', views.grades, name="grades"),
    path('fees/', views.fees, name="fees"),
    path('eval/', views.eval, name="eval"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('addSub/', views.addSub, name="addSub"),
    path('editSub/<int:pk>/', views.editSub, name="editSub"),
    path('deleteSub/<int:pk>/', views.deleteSubject, name="deleteSubject"),
    path('addSchedule/', views.addSchedule, name="addSchedule"),
    path('editSchedule/<int:pk>/', views.editSchedule, name="editSchedule"),
    path('deleteSchedule/<int:pk>/', views.deleteSchedule, name="deleteSchedule"),
    path('addGrade/', views.addGrade, name="addGrade"),
    path('editGrade/<int:pk>/', views.editGrade, name="editGrade"),
    path('deleteGrade/<int:pk>/', views.deleteGrade, name="deleteGrade"),
    path('addStudent/', views.addStudent, name="addStudent"),
    path('editStudent/<int:pk>/', views.editStudent, name="editStudent"),
    path('deleteStudent/<int:pk>/', views.deleteStudent, name="deleteStudent"),
    path('addProfessor/', views.addProfessor, name="addProfessor"),
    path('editProfessor/<int:pk>/', views.editProfessor, name="editProfessor"),
    path('deleteProfessor/<int:pk>/', views.deleteProfessor, name="deleteProfessor"),
]
