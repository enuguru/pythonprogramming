def read_employee_data(file_path):
    employees = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, emp_id, department, base_salary = line.strip().split(',')
                employees.append({
                    'name': name,
                    'id': emp_id,
                    'department': department,
                    'base_salary': float(base_salary)
                })
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return employees

def save_salary_report(file_path, report):
    try:
        with open(file_path, 'w') as file:
            file.write(report)
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")