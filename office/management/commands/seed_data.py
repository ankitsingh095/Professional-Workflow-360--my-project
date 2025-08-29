from django.core.management.base import BaseCommand
from office.models import Employee, Attendance
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Seed sample employees and attendance records'

    def handle(self, *args, **options):
        Employee.objects.all().delete()
        Attendance.objects.all().delete()
        names = [('Amit','Kumar'),('Priya','Sharma'),('Rahul','Verma'),('Sneha','Patel'),('Arjun','Rao')]
        for i,(f,l) in enumerate(names, start=1):
            e = Employee.objects.create(first_name=f,last_name=l,email=f.lower()+str(i)+'@example.com', salary=30000 + i*2000)
            for d in range(10):
                day = date.today() - timedelta(days=d)
                status = random.choices(['present','absent'], weights=[0.9,0.1])[0]
                Attendance.objects.create(employee=e, date=day, status=status)
        self.stdout.write(self.style.SUCCESS('Seeded sample employees and attendance.'))
