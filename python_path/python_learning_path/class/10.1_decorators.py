def check_access(func):
    def wrapper(employee):
        # Check if the employee has access to the function: Role "admin"
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print("You do not have access to this function")
    return wrapper

@check_access
def delete_employee(employee):
    print(f"Deleting {employee['name']} from the database")


admin = {'name': 'John', 'role': 'admin'}
employee = {'name': 'Jane', 'role': 'employee'}

delete_employee(admin) # Result: Deleting John from the database
#delete_employee(employee) # Result: You do not have access to this function