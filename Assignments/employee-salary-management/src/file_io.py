def save_report_to_file(report, filename):
    with open(filename, 'w') as file:
        file.write(report)

def load_employee_data_from_file(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:  # Assuming the format: name, ID, department, base_salary
                    name, emp_id, department, base_salary = data
                    employees.append({
                        'name': name,
                        'id': emp_id,
                        'department': department,
                        'base_salary': float(base_salary)
                    })
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return employees