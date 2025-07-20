# main.py

from employee import Employee
from tax_calculator import calculate_tax
from salary_report import generate_salary_report
from file_io import save_report_to_file, read_employee_data

def main():
    employees = []
    
    while True:
        print("Employee Salary Management System")
        print("1. Add Employee")
        print("2. Calculate Salary")
        print("3. Generate Salary Report")
        print("4. List Employees by Department")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            department = input("Enter department: ")
            base_salary = float(input("Enter base salary: "))
            employee = Employee(name, emp_id, department, base_salary)
            employees.append(employee)
            print("Employee added successfully.")
        
        elif choice == '2':
            emp_id = input("Enter employee ID to calculate salary: ")
            employee = next((emp for emp in employees if emp.emp_id == emp_id), None)
            if employee:
                tax = calculate_tax(employee.base_salary)
                net_pay = employee.base_salary - tax
                print(f"Net Pay for {employee.name}: {net_pay}")
            else:
                print("Employee not found.")
        
        elif choice == '3':
            emp_id = input("Enter employee ID to generate report: ")
            employee = next((emp for emp in employees if emp.emp_id == emp_id), None)
            if employee:
                report = generate_salary_report(employee)
                print(report)
                save_report_to_file(report, f"{employee.name}_salary_report.txt")
                print("Report saved successfully.")
            else:
                print("Employee not found.")
        
        elif choice == '4':
            department = input("Enter department to list employees: ")
            dept_employees = [emp for emp in employees if emp.department == department]
            if dept_employees:
                print(f"Employees in {department}:")
                for emp in dept_employees:
                    print(emp.name)
            else:
                print("No employees found in this department.")
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()