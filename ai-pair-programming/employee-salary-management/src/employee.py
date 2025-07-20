class Employee:
    def __init__(self, name, emp_id, department, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.base_salary = base_salary

    def get_employee_details(self):
        return {
            "Name": self.name,
            "ID": self.emp_id,
            "Department": self.department,
            "Base Salary": self.base_salary
        }