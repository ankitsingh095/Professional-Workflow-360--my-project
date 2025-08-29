from django.shortcuts import render, redirect
from .models import Employee, Attendance, Payroll
from .forms import EmployeeForm, AttendanceForm
from django.db import transaction

def index(request):
    employees = Employee.objects.all()
    return render(request, 'office/index.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'office/employee_form.html', {'form': form})

def attendance_list(request):
    attendances = Attendance.objects.select_related('employee').order_by('-date')[:50]
    form = AttendanceForm()
    return render(request, 'office/attendance_list.html', {'attendances': attendances, 'form': form})

def attendance_add(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
            except Exception as e:
                return render(request, 'office/error.html', {'error': str(e)})
    return redirect('attendance_list')

def payroll_run(request):
    month = request.GET.get('month')
    if not month:
        return render(request, 'office/error.html', {'error': 'Provide month e.g. ?month=2024-08'})
    employees = Employee.objects.all()
    results = []
    for emp in employees:
        # simple absent days count for month
        absent_days = Attendance.objects.filter(employee=emp, status='absent').count()
        daily_rate = float(emp.salary)/30.0 if emp.salary else 0
        deductions = round(absent_days * daily_rate,2)
        base = float(emp.salary)
        net = round(base - deductions,2)
        p, created = Payroll.objects.get_or_create(employee=emp, month=month, defaults={
            'base_salary': base, 'deductions': deductions, 'net_salary': net
        })
        if not created:
            p.deductions = deductions; p.net_salary = net; p.save()
        results.append({'employee': str(emp), 'net': net, 'deductions': deductions})
    return render(request, 'office/payroll_report.html', {'results': results, 'month': month})
