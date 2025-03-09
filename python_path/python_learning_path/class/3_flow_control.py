print('\n\n\nConditional estructures ---------------------------------')

x = 5

if x > 5:
    print('X is higher than 5')
    print('This condition is inside the if')
elif x == 5:
    print('X is equal than 5')
else:
    print('X is less than 5')



#new example 'and'
x1 = 15
y1 = 20

if x1 > 10 and y1 > 25:
    print('X is higher than 10 and higher than 20')

#new example 'or'
if x1 > 10 or y1 > 25:
    print('X is higher than 10')

#new example 'not'
if not x1 > 10:
    print('X is not higher than 10')


# niddle if:

is_member = True
age = 15

if is_menber:
    if age >= 15:
        print("You have access because you're member and you're or over 15 years old")
    else:
        print("You don't have access because you're member and you're not over 15 years old")
else:
    print("You don't have access because you're not member and you're not over 15 years old")



print('---------------------------------')


print('\n\n\nLoops and Iteration controls ---------------------------------')

#for

number_loop = [1, 2, 3, 4, 5, 6]

for i in number_loop:
    i+1
    print("i is = ", i)


for i in range(11):
    print(i)

fruits = ["Apple", "grapes", "orange", "Tomatoes", "bananas"]

for fruit in fruits:
    if fruit == "orange":
        print("Orange found")
        break
    else:
        print("Orange not found")


#for, continue
number_loop_while = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in number_loop_while:
    if i == 3:
        continue # The loops avoid to print i when its value is 3
    print("Hera i is = ", i)


#while, break
xyz = 0

while xyz < 10:
    if xyz == 7:
        break # As soon as xyz gets 7 as a value, the loop will end.
    print(xyz)
    xyz += 1




print('---------------------------------')



print('\n\n\nGenerators and operators ---------------------------------')

#--- iterators --- allow us to work with lists more eficiently, you can iterate each value in the list without saving all the values in memory at the same time.

# 1 Create a list
my_iterable_list = [1, 2, 3, 4]


# 2 obtain the iterator
my_iter = iter(my_iterable_list)

# 3 USe the operator
print(next(my_iter)) #Function next help us to see what values are being saving in memory each time. This line prints 1 because 1 is the first value iterated.
print(next(my_iter)) #This line prints 2
print(next(my_iter)) #This line prints 3
print(next(my_iter)) #This line prints 4


# 2 example: iterate in strings

#create the string
my_iterable_string = "Hello World"

#Obtain the iterator
my_iter_string = iter(my_iterable_string)

#use the operator
print(next(my_iter_string)) #H
print(next(my_iter_string)) #e
print(next(my_iter_string)) #l
print(next(my_iter_string)) #l
print(next(my_iter_string)) #o
print(next(my_iter_string)) #
print(next(my_iter_string)) #w
print(next(my_iter_string)) #o
print(next(my_iter_string)) #r
print(next(my_iter_string)) #l
print(next(my_iter_string)) #d


#Example 3 PRinting odd numbers

# Limit
limit = 10

#create iterator
odd_itter = iter(range(1,limit+1,2)) #the function iter is taking a range between 1 and 10, each time iter takes a value it adds 1 and the third parameter in the parenteses "2" is how many jumps the iterator will make for each interaction, so If it starts to iterate fron 1 it will take 3, then 5, then 7 until it reachs the limit "10" printing just the odds.

#Use the iterator, getting odd numbers
for num in odd_itter:
    print(num)



#--- Generators --- Its a function that allow us to create a secuence of number that we can iterate.

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


#second example , Fibonacci secuence: This secuence obtains a new value adding the tow previous ones
# 0 1 1 2 3 5 8 13 21 34 55...



def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(100):
    print(num)


#Sr. Code:
def fibonacci(limit: int) -> iter:
    if limit <= 0:
        raise ValueError("Limit must be a positive integer greater than 0")
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

def get_input() -> int:
    try:
        user_input = input("Enter the limit for the Fibonacci sequence: ")
        limit = int(user_input)
        if limit <= 0:
            raise ValueError("Limit must be a possitive integer")
        return limit
    except ValueError as e:
        print(f"Error: {e}")
        return get_input()

if __name__ == "__main__":
    limit = get_input()
    for num in fibonacci(limit):
        print(num)

print('---------------------------------')
