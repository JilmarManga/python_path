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
