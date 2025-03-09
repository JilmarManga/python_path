# Writing pythonic and profesional code:


print('\n\n\n Pythons good practices ---------------------------------')

print('\n\n\n Non eficient code ---------------------------------')

# Non eficient code:

"""numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)"""


print('\n\n\n eficient code = comprehencion list---------------------------------')

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers] # this reduces the last code to 2 lines and the result is the same
print(squares)


