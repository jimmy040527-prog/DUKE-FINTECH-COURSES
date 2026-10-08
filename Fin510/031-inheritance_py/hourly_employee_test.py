import pytest
from decimal import Decimal
from hourly_employee import HourlyEmployee
from employee import Employee


@pytest.fixture(autouse=True)
def reset_employee_id():
    Employee._Employee__id = 100


def test_create():
    a = HourlyEmployee("Max", "System Administrator", 65.0)
    assert a.name == "Max"
    assert a.job_title == "System Administrator"
    assert str(a) == "ID #100: Max(System Administrator, hourly)"


def test_compute_pay_no_hours():
    a = HourlyEmployee("Max", "System Administrator", 65.0)
    with pytest.raises((TypeError, AssertionError)):
        a.calculate_pay()


def test_compute_pay():
    a = HourlyEmployee("Max", "System Administrator", 65.0)
    a.hours_worked = 20
    assert a.calculate_pay() == Decimal(1300.0)
    a.hours_worked = 40
    assert a.calculate_pay() == Decimal(2600.0)


def test_compute_pay_with_overtime():
    a = HourlyEmployee("Max", "System Administrator", 65.0)
    a.hours_worked = 60
    assert a.calculate_pay() == Decimal(4550.0)


def test_employee_types():
    a = HourlyEmployee("Max", "System Administrator", 65.0)
    b = Employee("Cindy", "Sales Manager")
    assert a.employee_type == "hourly"
    assert a.employee_type != b.employee_type
