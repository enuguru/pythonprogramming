# Employee Salary Management System

This project is an Employee Salary Management System implemented in Python. It provides functionalities for managing employee data, calculating taxes, generating salary reports, and handling file I/O operations.

## Project Structure

```
employee-salary-management
├── src
│   ├── employee.py        # Defines the Employee class and its properties
│   ├── tax.py             # Contains functions for tax calculation
│   ├── report.py          # Generates formatted salary reports
│   ├── file_io.py         # Handles file reading and writing
│   └── main.py            # Command-line interface for the application
├── requirements.txt       # Lists project dependencies (if any)
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd employee-salary-management
   ```

2. Ensure you have Python installed on your machine.

3. Navigate to the `src` directory:
   ```
   cd src
   ```

## Usage

To run the application, execute the `main.py` file:

```
python main.py
```

## Functionality

- **Employee Management**: Add and manage employee details including name, ID, department, and base salary.
- **Tax Calculation**: Calculate taxes based on the employee's salary using predefined rules.
- **Salary Report Generation**: Generate and format salary reports for employees, including net pay calculations.
- **File I/O Operations**: Save salary reports to text files and load employee data from files.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.