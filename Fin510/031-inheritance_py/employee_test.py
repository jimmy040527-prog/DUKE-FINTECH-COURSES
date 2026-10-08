import ast
import pytest
from employee import Employee


@pytest.fixture(autouse=True)
def reset_employee_id():
    Employee._Employee__id = 100


def test_create():
    a = Employee("Steve", "Programmer")
    b = Employee("Christine", "Project Manager")
    assert a.id != b.id
    assert a.name == "Steve"
    assert b.name == "Christine"
    assert a.job_title == "Programmer"
    assert b.job_title == "Project Manager"
    assert str(a) == "ID #100: Steve(Programmer, unknown)"
    assert ast.literal_eval(repr(b)) == {'id': 101, 'name': 'Christine', 'job_title': 'Project Manager'}


def test_calculate_pay_not_implemented():
    a = Employee("Steve", "Programmer")
    with pytest.raises(NotImplementedError, match="must implement"):
        a.calculate_pay()


def test_change_job_title():
    a = Employee("Steve", "Programmer")
    a.job_title = 'Senior Programmer'
    assert a.job_title == 'Senior Programmer'
    assert str(a) == "ID #100: Steve(Senior Programmer, unknown)"
