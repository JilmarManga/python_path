print('\n\n\nFunctions ---------------------------------')


def greet(name, last_name="Not last name registered"):
    print("Hello,", name, last_name)

greet("Jilmar", "Manga")
greet("Jilmar",) #It takes the default value asigned to the parameter

#Calculator

def add(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def calculator():
    while True:
        print('Selec an option:\n1. Add\n2. subtraction\n3. Multiplication\n4. Division\n5. Salir')

        option = input("Enter your option: ")

        if option == "5":
            print("Finishing calculator")
            break

        if option in ["1","2","3","4","5"]:
            num1 = int(input("Enter the first value: "))
            num2 = int(input("Enter the second value: "))

            if option == "1":
                print("Add is: ", add(num1, num2))
                break
            elif option == "2":
                print("Subtraction is: ", subtraction(num1, num2))
                break
            elif option == "3":
                print("Multiplication is: ", multiplication(num1, num2))
                break
            elif option == "4":
                print("Division is: ", division(num1, num2))
                break
        else:
            print("Non valid option, please try again")

calculator()


print('---------------------------------')

print('\n\n\n Lambda Functions and functional programing---------------------------------')

add = lambda a, b: a+b
print(add(10,4))

#Obtaion square of each number
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Results squared numbers: ", squared_numbers)

#even numbers
even_numbers = list(filter(lambda x: x%2 == 0, numbers))#The method filter, filter the results with the conditional between parenthesys
print("Even numbers: ", even_numbers)

print('---------------------------------')


print('\n\n\n Recursive Functions ---------------------------------')

#Hallar el factorial de 4 y 5:
    #base Case : When the number == 0
    #rescursive Case: When the number > 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_5 = print(factorial(5))


#Hallar la secuencia de Fibonacci:
    #base Case : When the number == 0: 0
    #Recursive case: When the number == 1: F(n-1) + F(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + (n-2)

number = 3
print(fibonacci(number))

#calculate the addition of natural numbers ej: given_number = 5: return: 5+4+3+2+1

def natural_numbers_add(i):
    if i == 0:
        return 0
    else:
        return i + natural_numbers_add(i-1)

print(natural_numbers_add(5))


print('---------------------------------')



print('\n\n\n Errors and exceptions ---------------------------------')

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# PRinting the jerarqui starting from the base class exception
print_exception_hierarchy(Exception)


try:
    divisor = int(input("Enter a division number: "))
    result =100/divisor
    print(result)
except ZeroDivisionError:
    print("Error: Division number can't be zero")
except ValueError as e: #capturing the error in a variable "e"
    print(f"Error: {e}") #concatening the especific error storadge in the variable "e" and printing it.



print('---------------------------------')

