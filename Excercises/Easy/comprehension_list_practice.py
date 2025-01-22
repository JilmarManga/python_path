'''
1- Doble de los Números
Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.'''


number_list = [1, 2, 3, 4, 5]

square_number = [x * 2 for x in number_list]
print(square_number)



'''2- Filtrar y Transformar en un Solo Paso
Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.'''


word_list = ["sol", "mar", "montaña", "rio", "estrella"]

new_list = [word.upper() for word in word_list if len(word) > 3]
print(new_list)


'''3- Crear un Diccionario con List Comprehension
Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.'''

keys = ["name", "age", "ocupation"]
values = ["Juan", 30, "engineer"]

#Soluction method 1
dictionary = {key : value for key, value in zip(keys, values)}
print('method 1 =', dictionary)

#Solution method 2
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print('method 2 =', dictionary)

#Exercise #2

list1 = ['model', 'year', 'color']
list2 = ['CX-90', '2025', 'white']

#method 1
dictionary1 = {list_keys : list_values for list_keys, list_values in zip(list1, list2)}
print(dictionary1)

#method 2
dictionary2 = {list1[i] : list2[i] for i in range(len(list1))}
print(dictionary2)



'''4- Anidación de List Comprehensions
Dada una lista de listas (una matriz):

pythonCopiar código
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Calcula la matriz traspuesta utilizando una List Comprehension anidada.'''


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)


matrix2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

transposed_matrix_2 = [[row[i] for row in matrix2] for i in range(len(matrix2[0]))]
print(transposed_matrix_2)


'''5- Extraer Información de una Lista de Diccionarios
Dada una lista de diccionarios que representan personas:

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.'''

people = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

new_list_people = [person['nombre'] for person in people if person["ciudad"] == 'Madrid' and person["edad"] > 30]
print(new_list_people)


'''6- List Comprehension con un else
Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.'''


number_list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_even_numbers = [num * 2 if num % 2 == 0 else num for num in number_list_6]
print(square_even_numbers)