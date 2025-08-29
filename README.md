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

## How the features map to the resume bullets
- **Integrated attendance, payroll, and employee lifecycle modules**: The `office` app centralizes models and UI for employees, attendance, and payroll. Payroll computation uses attendance data to apply deductions and stores payroll records in the `Payroll` model.

- **Scalable design (Python + Django)**: Uses Django's ORM, transactions, and admin — the structure allows adding more modules, endpoints or background jobs (Celery) without changing core models.

- **Bootstrap responsive UI**: Templates use Bootstrap 5 CDN. Pages are mobile-friendly and recruiter-ready.

## Interview prep — How to explain this project (easy script)
1. Problem solved: centralize HR operations (attendance, payroll) in a simple web app to reduce manual errors and speed up processing.
2. Tech used: Django for backend + ORM, Bootstrap for responsive front-end.
3. Implementation details:
   - Models: `Employee`, `Attendance`, `Payroll`.
   - Payroll processing reads attendance and computes deductions for absences, storing results.
   - Admin UI allows HR to view and correct records.
4. How it achieves the claimed improvements (talk track):
   - Reduction in payroll processing time: automation of calculations and single-click payroll run eliminates manual Excel work.
   - Fewer errors: validations, unique constraints (unique_together), and atomic DB transactions reduce synchronization mistakes.
   - Responsive UI: Bootstrap reduces UI development time and improves data entry accuracy.

## Files included
- Django project `workflow360/` and app `office/`
- `requirements.txt` and `README.md`
- `manage.py` and a management command `seed_data` to populate demo data

## Notes
This is a compact demo intended for portfolio and interview demonstration. For production, add authentication, background tasks for payroll, audit logs and tests.
