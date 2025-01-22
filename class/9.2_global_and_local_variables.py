print('\n\n\n local variables "local scope"---------------------------------')

def local_function():
    x = 10 #Local variable
    print(f"The value of the variable x is: {x}")

local_function() #This line prints in console the value storadged in the variable X

#print(x) #This line generated error because it is trying to print a local variable, this kinds of variables can just be user while the function is excecuted.

print('\n\n\n global variables "global scope"---------------------------------')

m = 100 # Global variable

def show_global():
    print(f"The value of the variable m is: {m}")

show_global() #This line prints in console the value storadged in the variable m, it is possob;le to print the value because the variable "m" is global, means it can be called even if it is not declarated on a function


print('\n\n\n Inner functions "local scope"---------------------------------')

y = "global" #Global variable

#external function
def outer_function():
    y = "enclosing"
    #Inner function
    def inner_function():
        y = "local" # Local variable
        print(y) # This line is gonna be printed at firts

    inner_function() #Calling the inner function
    print(y) #Printing the value of the variable "y" in the "outer_function"

outer_function() #Calling the outer_function
print(y) #printing the valie storage in "y" as a global variable


print('\n\n\n Keyword ""Global"---------------------------------')

z = 5 # Global variable

def modify_global():
    global z
    z+=3
    print(f"modified value: {z}")

modify_global()
print(z)


print('\n\n\n non-local variables ---------------------------------')

"""A nonlocal variable in Python is a variable that exists in an enclosing scope (not the global scope) and is accessed or modified within a nested function. It allows a nested function to change the value of a variable defined in its outer (enclosing) function.

Key Characteristics of nonlocal Variables:
	1.	Not Local, Not Global:
	•	The variable is not defined in the current function’s local scope but is also not in the global scope. It exists in an intermediate, enclosing scope.

    2.	Modifiable:
	•	By using the nonlocal keyword, you can modify the variable from within the nested function.

    3.	Useful for Closures:
	•	Frequently used in closures where the nested function needs to retain state or modify a variable in the outer function.
"""

def outer_function():
    x = "enclosing"
    def inner_function():
        nonlocal x
        x = "modified"
        print(f"The value in Inner is: {x}")
    inner_function()
    print(f"The value in outer is: {x}")
outer_function()


# Comparison between non-local and global scope

"""
	•	global: Refers to variables in the global scope, accessible from anywhere in the program.
	•	nonlocal: Refers to variables in an enclosing function’s scope (not global), accessible only from nested functions.
"""

x = 10  # Global variable

def outer_function():
    x = 5  # Enclosing variable (local to outer_function)

    def inner_function():
        global x  # Refers to the global 'x'
        x += 1
        print(f"Global x is now: {x}")

    inner_function()
    print(f"Enclosing x remains: {x}")

outer_function()