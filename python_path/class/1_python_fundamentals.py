person = 'Jilmar'

print(person)
print('Here we go again')


#Strings
name = 'Jilmar'
caracter = 'C'
print(type(name))
print(type(caracter))

print('Nunca','pares','de','aprender')


#Parameters:
    #sep : Allow you how to separate the elements when printing, in this case the message will be printed with a , and space betwen the words.
print('Nunca','pares','de','aprender',sep=', ')


    #end : this parameter changes what will be printed at the end of the line
print('Nunca',end=' ')
print('pares de aprender')



#Special Caracters>
    #Salto de linea
print('Hola\nMundo')

    #Quotes: \'
print('Hello I\'m Jilmar, but you can call me \'AJ\'')

    #slash, paths, endpoints: \'
print('The file\'s endpoint is: C:\\Users\\Usuario\\Desktop\\archivo.txt')


#Index
name2 = 'Jilmar Manga'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print('---------------------')

#reverse index
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])

print('---------------------')


#Concatenacion
name = 'Jilmar'
lastName = 'Manga'

print(name + ' ' + lastName)


#Replication
print(lastName * 5)

#Function length : this methond returns how length a string is
print(len(name))


#Methods
print(name.upper())
x = 10
y = 10.58
z = 10.4E-6

print(type(x))
print(type(y))
print(type(z))

#Format:
    #Format with 'f-strings'
phrase = 'Never stop learning'
author = 'Platzi'
print(f'Phrase: {phrase}, Author: {author}')

    #Format with 'format'
phrase = 'Nunca pares de aprender'
author = 'Platzi'
print('Phrase: {}, Author: {}'.format(phrase, author))

    #Print with specific format
value = 3.14159
print('Value:{:.2f}'.format(value))

#Add

print(x + y + z)

#Boolenas
ifItsTrue = True
ifItsFalse = False

print(ifItsTrue)
print(type(ifItsFalse))


print('\n\n\nMathematical operations in python ---------------------------------')



#Mathematical operations in python:

    #mathematical operators
a = 10
b = 3

print('Add:', a + b) #13
print('sustraction:', a - b) #7
print('Multiplicacion:', a * b) #30
print('Division:', a / b) #3.3
print('Parte entera de la Division:', a // b) #3
print('Module:', a % b) #1
print('Potenciacion:', a ** b) #1

    #shortcuts
a += 2 #This is the same as a = a + 2
print(a) #12

a **= 2 #This is the same as a = a ** 2
print(a) #144

    #When it is necesario resove mathematical operations more complex we must follow the PEMDAS rule!
    #Parenteses
    #Exponents
    #Multiplicaction
    #Division
    #addition
    #Subtraction

operation1 = 2 + 3 * 4
operation2 = (2 + 3) * 4
operation3 = 2 + (3 * 4)
operation4 = (2+3) * (4**2) / 8 - 1

print(operation1)
print(operation2)
print(operation3)
print(operation4)

    #Booleans
print( a > b)
print( a < b)
print( a >= b)
print( a <= b)
print( a == b)
print( a != b)


print('\n\n\nOperations input / output ---------------------------------')

#Imput: the data type in imput is always going to be string

'''name = input('Name: ')
age = input('age: ')
print(name, age)
print(type(name))
print(type(age))

    #Casting: We can especify the date type waited:

name1 = input('Name1: ')
age1 = int(input('age2: '))
print(name, age)
print(type(name1))
print(type(age1))'''



print('\n\n\nCondicionals ---------------------------------')


#If

x = 5
if x > 5:
    print(x, 'is greater than 5')
elif x == 5:
    print(x, 'is equal to 5')
else:
    print(x, 'is less than 5')


y = 15
z = 20

if y > 10 and z > 25:
    print('True')

if y > 10 or z > 25:
    print('False')

if not z > 25:
    print('z is not greater than 10')


#Nested if:

is_menber = True
age = 30

if is_menber:
    if age >= 15:
        print('Your access has been authorized because you ae a menber and you are 15 or more')
    else:
        print('Your access has been denied because you are menber but you are not 15 yet')
else:
    print('Access denied because you are not menber')



