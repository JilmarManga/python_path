# __name__ : executa the code directly

'''
Advantages:

- Modularity: Reuses the code without auto-executing it.
- Debboging test: Executes tests or debbuginf when executes the script directly without running the entire program.
- Direct execution: makes eassy that a file works as an executable script.
'''

def add(num1: str, num2: str) -> str:
    return num1 + num2

def substract(num1: str, num2: str) -> str:
    return num1 - num2

def multiply(num1: str, num2: str) -> str:
    return num1 * num2

def divide(num1: str, num2: str) -> str:
    if num2 == 0:
        raise ValueError('Cannot divide by zero')
    return num1 / num2

if __name__ == '__main__':
    print('Operations')
    res_1 = add(5, 3)
    print(f'Addition: {res_1}')
    print(f'Division: {divide(10,7)}')


print('\n\n\n Activity: Add and delete employees ---------------------------------')


Employee_list = [
    {'name': 'John', 'age': 28, 'salary': 50000, 'worker_id': 1254258},
    {'name': 'Jane', 'age': 25, 'salary': 60000, 'worker_id': 1845628},
    {'name': 'Doe', 'age': 30, 'salary': 70000, 'worker_id': 9756842}
]

def add_employee(employees, name, age, salary, worker_id):
    #add employee to the list
    employees.append({'name': name, 'age': age, 'salary': salary, 'worker_id': worker_id})
    print(f'Employee {name} added successfully.')

def delete_employee(employees, name, worker_id):
    #delete employee by name and worker_id from the list, if found
    for employee in employees:
        if employee['name'] == name and employee['worker_id'] == worker_id:
            employees.remove(employee)
            print(f'Employee {name} deleted successfully.')
            return
    print(f'Employee {name} not found in the list.')

if __name__ == '__main__':
    # Previwe of the lits:
    print('Employee list:', Employee_list)

    # Add an employee
    add_employee(Employee_list, 'Alice', 30, 70000, 123456)
    add_employee(Employee_list, 'Bob', 35, 80000, 123457)

    # Display the list after adding employees:
    print(f'\nCurrent employee list:', Employee_list)

    #Delete employees:
    delete_employee(Employee_list, 'Alice', 123456)
    delete_employee(Employee_list, 'John', 1254258)

    # Display the list after deleting employees:
    print(f'\nNew employee list:', Employee_list)