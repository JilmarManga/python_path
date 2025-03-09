print(' args ---------------------------------')
# args = data type tuple

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 15
print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(1, 2))  # 3
print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
print(sum_numbers(*range(1, 101)))  # 5050

print('\n\n kwargs ---------------------------------')
# kwargs = data tipe dictionary

def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_values(name="John", age=25, city="New York")
print_values(name="Jane", age=30, city="San Francisco", job="Engineer")


print('\n\n args and kwargs in Classes ---------------------------------')

class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.detail = kwargs

    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills:', self.skills)
        print('Details:', self.detail)


employee = Employee('John', 'Python', 'Java', 'C++', age=25, city='New York')
employee.show_employee()


print('\n\n Unpacking ---------------------------------')
#Unpacking

#Unpacking args
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
print(add(*values)) # External variable 'values' is taking as args

#Unpacking kwargs
def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

data = {"name": "Ana", "age": 28}
show_info(**data) # External variable 'data' is taking as kwargs



print('\n\n Unpacking Activity ---------------------------------')

'''
create a function that receives n products and their prices, calculate the total and apply an optional discount if it is given as an argument with name, use args for receiving a list of prices and kwargs for accepting an optinal discount and appying to the total 
'''

def calculat_total(*prices, **kwargs):
    #Calculate the toal prices of products and apply an optional discount.
    total = sum(prices) # Sum all the products prices
    discount = kwargs.get('discount', 0) # Get the discount value or 0 if not provided

    if discount:
        total -= total * (discount / 100) # Apply the discount if it is provided
    return round(total, 2) # Return the total rounded to 2 decimal places

# Test the function
print(calculat_total(100, 200, 300, 400, discount=10)) # 900.0, 10% discount applied
print(calculat_total(10, 20, 30, 40)) # 100.0, no discount applied