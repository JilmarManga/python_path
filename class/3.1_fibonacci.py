
# --- Practicing generators ---


# Simple code

def fibonacci(limit = input()):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(100):
    print(num)


#Sr. Code:
def fibonacci(limit: int) -> iter: #Fibonacci operator
    if limit <= 0:
        raise ValueError("Limit must be a positive integer greater than 0") # Error integer validator
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b # Math operation

def get_input() -> int: # Input checker
    try:
        user_input = input("Enter the limit for the Fibonacci sequence: ")
        limit = int(user_input)
        if limit <= 0:
            raise ValueError("Limit must be a possitive integer") #Error Manager
        return limit
    except ValueError as e:
        print(f"Error: {e}") # Error printing
        return get_input()

if __name__ == "__main__": #function trigger
    limit = get_input()
    for num in fibonacci(limit):
        print(num)


# --- Practicing generators --- : Odd numbers Simple code.

def odd_numbers(limit):
    a = 1
    while a < limit+1:
        yield a
        a = a+2

for num in odd_numbers(10):
    print(num)


# --- Practicing generators --- : even numbers Sr code.

#math function
def even_numbers(limit: int):
    if limit < 0:
        raise ValueError("Limit must be a positive integer greater than 0") # Error integer validator
    a = 0
    while a < limit+1:
        yield a
        a = a+2 # Math operation

#input Checker
def get_input() -> int:
    try:
        user_input = input("Enter the limit for the sequence: ")
        limit = int(user_input)
        if limit <= 0:
            raise ValueError("Limit must be a possitive integer") #Error Manager
        return limit
    except ValueError as e:
        print(f"Error: {e}") #Error Printing
        return get_input()

#function trigger
if __name__ == "__main__":
    limit = get_input()
    for num in even_numbers(limit):
        print(num)