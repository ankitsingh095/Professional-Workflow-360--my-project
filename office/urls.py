from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_add, name='attendance_add'),
    path('payroll/run/', views.payroll_run, name='payroll_run'),
]
