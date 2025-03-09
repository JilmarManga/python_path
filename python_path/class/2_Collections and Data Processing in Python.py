print('\n\n\nClass : Lists ---------------------------------')

to_do = ['Mazda',
        'BMW',
        'Mercedez',
        'Range Rover']
print(to_do)

numbers = [1, 2, 3, 4, 'Cinco']
print('Numbers is type :', type(numbers))

mix = ['uno', 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print('First element of mix:', mix[0])
print('Second element of mix:', mix[1])
print('Last element of mix:', mix[-1])
print('First 3 elements of mix:', mix[0:3])
print('From second to the last element of mix:', mix[1:])
print('From first to the fouth element of mix:', mix[:4])

    #append: how to add elements to a list
mix.append(False)
mix.append(['a', 'b'])
print('New mix: ', mix)

    #insert: how to add elements to a list in an specific index
mix.insert(1, ['a', 'b']) #first especify the position then the new element
print(mix)

    #ask the exact position of an element in the list
print(mix.index(['a','b'])) #this is going to show the just the first position

    #Filtering the highest and lowest number from a list
numbers = [1, 2, 3, 58, 64, 95, 112, 120]
type_numbers = 'Type: ', type(numbers)
print(numbers)
print(type_numbers)
print('Highest number of Numbers:',max(numbers))
print('Lowest number of Numbers:',min(numbers))

    #Deleting elements of the list
del numbers[-1] #DEleting the las element of the list
print(numbers)

del numbers[:3] #Deleting the 3 first elements from the list
print(numbers)

print('---------------------------------')


print('\n\n\n Class: Slice Method ---------------------------------')

    #Method Slice: this method copy the information of a variable into another but it does not use the same space in memry
a = [1,2,3,4,5,6]
b = a
print(a)
print(b)

del a[0]
print(a)
print(b)

c = a[:] #This is the slice method, in variable C we are copying the list stored in variable a from the first to the last item
print(c)

a.append(10.3)
print(a) #list in variable a should print the list whit the new value
print(c) #Lsit in variable c should print the original list storaged in the first variable a 'With out 10.3' 


print('---------------------------------')



print('\n\n\nClass : Matrices and Tuples ---------------------------------') 

    #Matrix
matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

print(matrix) #This is going to print the whole matrix
print(matrix[0]) #This is going to print first row
print(matrix[0][2]) #This is going to print the third item on the first row


    #Tuple
numbers = (1,2,3,4,5) #syntax to declare a tuple
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = 'uno' # this action generates error, beause tuples are inmutable, means they can't be changed or alterated.

print('---------------------------------')


print('\n\n\nDictionaries ---------------------------------')

#To especify the use of dictionaries we must use {}

dictionary = {1:'uno', 2:'dos', 3:'tres'}
print(dictionary[2]) #We can acces to the specific piece of data using the number where it was asigned.

information = {'Name': 'Jilmar', #key : value format
                'Last name': 'Manga',
                'Heigh': '1.70',
                'Age': '31'}
print(information)

#del information['age']
print(information)

key = information.keys() #Storage in a new variable the keys of the dictionarie 'infromation' using the method .keys()
print('Keys:', key)
print(type(key))

value = information.values() ##Storage in a new variable the values of the dictionarie 'infromation' using the method .values()
print('Values:', value)
print(type(value))

pairs = information.items() ##Storage in a new variable the pairs key : value of the dictionarie 'infromation' using the method .items()
print('Pairs:', pairs)
print(type(pairs))

    #Dictionary of dictionaries
contacts = {'Jilmar': {'Last name': 'Manga', #when we asked for the name Jilmar it will give us the information storage in the {} after the name
                'Heigh': '1.70',
                'Age': '31'},
            'Jennyfer': {'Last name': 'Manga',
                'Heigh': '1.65',
                'Age': '28'},
            'Amanda': {'Last name': 'Torres',
                'Heigh': '1.56',
                'Age': '58'},
            'Sergio': {'Last name': 'Manga',
                'Heigh': '1.65',
                'Age': '59'}}

print(contacts)
print(contacts['Amanda']) #Checking just the information of the name Amanda

print('---------------------------------')


print('\n\n\nComprehension Lists ---------------------------------')

#1 Calculate the square of the numbers stored in the list square
squares = [x ** 2 for x in range(1, 11)]
print('Squares:', squares)


#2 Calculate the temperature in Farenheit from the given celsius temperature
celsius = [0, 10, 20, 30, 40]
farenheit = [(temp * 9/5) * 32 for temp in celsius]
print('Temperature in F = ', farenheit)


#3 Finding evens numbers in from the given list of numbers
evens = [x for x in range (1, 101) if x % 2 == 0]
print(evens)
output_evens_list = ('\n'.join(map(str, evens))) #This print every number of the resoult in a new line
print(output_evens_list)


#4 Transpose a matriz

    #with several lines of code:

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
print(matrix)

transposed_one_line_of_code = [[row[i] for row in matrix] for i in range (len(matrix[0]))]

transpose = []
for i in range (len(matrix[0])):
    transpose_row = []
    #print(transpose_row)
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)

print('Traditional solution', transpose)


    #with just one line of code using comprehension lists:

transposed_one_line_of_code = [[row[i] for row in matrix] for i in range (len(matrix[0]))]
print('Comprehension list solution: ', transposed_one_line_of_code)
