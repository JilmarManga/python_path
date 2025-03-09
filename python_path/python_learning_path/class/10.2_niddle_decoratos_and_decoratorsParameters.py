'''Niddle Decorators and Decorators Parameters are used to add extra functionality to a function, they are very important
to make the code more readable, efficient and easy to maintain. With this techniques you can write code highly reusable, personalized and modular accordingly to your needs, especially for complex big-scale projects where it is require extra controls on the execution flow. In this example we are going to create a decorator that checks if an employee has access to a function based on his role. We are going to use a decorator with parameters to make the code more flexible and reusable'''


# Decorator information pruves if an employee has a specific role
def check_access(role):
    def check_access_decorator(func):
        def wrapper(employee):
            # Check if the employee has access to the function: Role "admin"
            if employee.get('role') == role:
                return func(employee)
            else:
                print(f"You do not have access to this function, just {role} can access")
        return wrapper
    return check_access_decorator


def log_action(func):
    def wrapper(employee):
        print(f"Action performed by {employee['name']}")
        return func(employee)
    return wrapper


@check_access('admin')
@log_action
def delete_employee(employee):
    print(f"Deleting {employee['name']} from the database")


admin = {'name': 'John', 'role': 'admin'}
employee = {'name': 'Jane', 'role': 'employee'}

#delete_employee(admin)  # Result: Deleting John from the database
delete_employee(employee)  # Result: You do not have access to this function