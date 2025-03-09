"""
Anotations are used to give clarity about the code that we are writing, most of all when we are working with developing teams.

types of anotations:
int: Integers
Float: numbers with float dot or decimal nunbers
str: text strings
bool: Booleans values
list: list
dict: dictionaries
tuple: Tuplas

"""

#variable withot anotations:
id1 = 101

#variable with anotations:
id2: int = 102 # this notations indicates that the variable has a varaible type "integer"


def number_of_computers_in_storage(whs1: int, whs2: int, whs3: int) -> int: #parameters have anotation, type of variable "integer" and the result of the function must be an integer
    return whs1 + whs2 + whs3
print(number_of_computers_in_storage(150, 200, 80))

print('\n\n\ ---------------------------------')

#Example with classes and objects

#Class
class Employee:
    name: str
    age: int
    salary: float
    id_number: int

    #Constructor function
    def __init__(self, name: str, age: int, salary: float, id_number: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.id_number = id_number

    #Method: Information on the data base
    def information_on_the_data_base(self) -> str:
        return f"Employyee number: {self.id_number}, name: {self.name}, age: {self.age}, salary: ${self.salary}"

# Building the object:
employee1 = Employee("Jilmar", 30, 20000, 210520)
print(employee1.information_on_the_data_base()) #print the method