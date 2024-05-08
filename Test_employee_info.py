#test_employee_info.py

import employee_info as ef

def test_age_range():
    result = ef.get_employees_by_age_range(20,30)
    exp_result = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]

    assert (result == exp_result)
    
    
def test_avg_salary():
    employee_data = [
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    
    result = ef.calculate_average_salary(employee_data)
    exp_result = 65000

    assert (result == exp_result)


def test_emp_dept():
    result = ef.get_employees_by_dept("Sales")

    exp_result = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
    ]

    assert (result == exp_result)