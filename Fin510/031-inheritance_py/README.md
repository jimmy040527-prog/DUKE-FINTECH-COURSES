# Inheritance

Based on the inheritance notebook, implement the classes for the 
`SalariedEmployee` and `CommisionedEmployee` classes.

The `SalariedEmployee` class should be defined in a file `salaried_employee.py` 
and have the following initializer method:
```python
def __init__(self, name, job_title, annual_pay_rate):
```



The  `CommissionedEmployee` class should be defined in a file 
`commissioned_employee.py` and have the following initializer method:
```python
def __init__(self, name, job_title, annual_pay_rate, period_gross_sales):
```

## Notes
- You need to implement the `calculate_pay()`  method and `employee_type` 
  property  (just the getter) for both classes.  `employee_type` should either 
  return "salaried" or "commissioned".
- Assume the employees are paid bi-monthly (i.e., twice a month), so their 
  periodic pay is 1/24 of their annual pay rate.
- A commissioned employee's salary is computed as the pay they would receive 
  as a salaried employee plus 5% of their period gross sales.

We have provided pytest test files (`employee_test.py`, `hourly_employee_test.py`) that test the provided base classes. You can run them with:
```bash
pytest employee_test.py
pytest hourly_employee_test.py
```

## Submission
Submit `salaried_employee.py` and `commissioned_employee.py` for grading.
