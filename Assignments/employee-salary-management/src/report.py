def generate_salary_report(employee):
    base_salary = employee.base_salary
    tax = calculate_tax(base_salary)
    net_pay = base_salary - tax

    report = f"Salary Report for {employee.name} (ID: {employee.id})\n"
    report += f"Department: {employee.department}\n"
    report += f"Base Salary: ${base_salary:.2f}\n"
    report += f"Tax Deducted: ${tax:.2f}\n"
    report += f"Net Pay: ${net_pay:.2f}\n"

    return report

def calculate_tax(base_salary):
    if base_salary < 50000:
        return base_salary * 0.10
    else:
        return base_salary * 0.20

def save_report_to_file(report, filename):
    with open(filename, 'w') as file:
        file.write(report)