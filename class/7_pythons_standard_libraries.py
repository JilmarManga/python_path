print('\n\n\nOS library ---------------------------------')

# OS library = Allows you to work with the operative system

import os

# Get cwd (current working directory)
cwd = os.getcwd()
print("Current working directory:", cwd)


#List .txt files
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")] # Comprehencion list taht list all the files in the current directory
print("txt files: ", txt_files)



print('\n\n\nmath library ---------------------------------')


import math

# math library = allow us to work with complex mathematical operations


# Get the area and perimeter of a circle
radius = 5
area = math.pi * radius **2
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)



print('\n\n\nrandom library ---------------------------------')

# Random library = It;s usefull for creating groups of aleatory numbers o creating aleatory behaviors to a existing groups

import random

#generating an aleatory integer number
random_number = random.randint(1,1000000)
print(random_number)


#Choose aleatory colors
colors = ["red", "blue", "green"]
random_color = random.choice(colors)
print(random_color)


# Shuffle a list of cards
cards = ["as", "king", "queen", "J", "10"]
random.shuffle(cards)
print(cards)