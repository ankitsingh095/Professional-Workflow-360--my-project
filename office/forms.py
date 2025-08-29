from django import forms
from .models import Employee, Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','email','join_date','salary']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee','date','status']
