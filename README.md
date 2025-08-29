# Professional Workflow 360

**Tech**: Python, Django, Bootstrap (2024)

A compact Office Management System containing integrated modules for **Attendance**, **Payroll**, and **Employee Lifecycle**. The project demonstrates:

- Integrated attendance, payroll, and employee lifecycle modules (Employee, Attendance, Payroll models + admin and UI).
- Responsive UI built with Bootstrap (via CDN) for quick, recruiter-friendly demo.
- A simple payroll processing view that computes net salary after deductions (absent days).

## Quick start
1. Create virtualenv and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run migrations and seed data:

```bash
python manage.py migrate
python manage.py seed_data
```

3. Start server:

```bash
python manage.py runserver
```

4. Open http://127.0.0.1:8000/ to view employees, attendance and payroll.

