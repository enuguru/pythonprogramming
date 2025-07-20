# main.py

from employee import Employee
from tax import calculate_tax
from report import generate_salary_report
from file_io import save_report_to_file, load_employee_data

def main():
    employees = []
    
    while True:
        print("Employee Salary Management System")
        print("1. Add Employee")
        print("2. Calculate Tax")
        print("3. Generate Salary Report")
        print("4. Save Report to File")
        print("5. Load Employee Data from File")
        print("6. Exit")
        
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
            emp_id = input("Enter employee ID to calculate tax: ")
            employee = next((emp for emp in employees if emp.emp_id == emp_id), None)
            if employee:
                tax = calculate_tax(employee.base_salary)
                print(f"Tax for {employee.name} (ID: {emp_id}): {tax}")
            else:
                print("Employee not found.")
        
        elif choice == '3':
            emp_id = input("Enter employee ID to generate report: ")
            employee = next((emp for emp in employees if emp.emp_id == emp_id), None)
            if employee:
                report = generate_salary_report(employee)
                print(report)
            else:
                print("Employee not found.")
        
        elif choice == '4':
            report = input("Enter report content to save: ")
            filename = input("Enter filename to save report: ")
            save_report_to_file(report, filename)
            print("Report saved successfully.")
        
        elif choice == '5':
            filename = input("Enter filename to load employee data: ")
            employees = load_employee_data(filename)
            print("Employee data loaded successfully.")
        
        elif choice == '6':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()