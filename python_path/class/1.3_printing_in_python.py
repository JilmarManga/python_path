'''

*** Everything You Need to Know about print in Python ***


Class
The built-in print function may seem basic at first, but keep in mind that it’s a tool you’ll use in multiple ways throughout your code. From the iconic “Hello, World!” to debugging messages and displaying results, print is the gateway for your programs to communicate with the outside world.

Starting with a simple “Hello, World!” is not only a tradition in programming but also a crucial moment where your code comes to life. It’s the first line of code that shows your development environment is correctly set up and you’re ready to start creating.

You will learn to make the most of the built-in print function in Python. From advanced formats to handling special characters and escape sequences, you’ll discover how print can be a powerful and versatile tool in your programming toolkit.

-- 1.	Basic Use of print
The simplest use of print involves passing the text you want to display within quotes. This code will print “Never stop learning” in the console, an excellent way to check if your Python environment is set up correctly.
'''

print("Never stop learning")

'''
Output:
Never stop learning
'''

'''
-- 2.	Using Comma in print
The comma within the print function is used to separate multiple arguments. When doing so, Python automatically adds a space between the arguments. This is different from concatenating strings with the + operator, which doesn’t add extra spaces.
'''

print("Never", "stop", "learning")

'''
Output:
Never stop learning
'''

'''
On the other hand, when concatenating strings with the + operator, the elements join without any extra space unless you add it explicitly.
'''

print("Never" + "stop" + "learning")

'''
Output:
Neverstoplearning
'''

'''
To add a space explicitly when concatenating strings, include it within the quotes.
'''

print("Never" + " " + "stop" + " " + "learning")

'''
Output:
Never stop learning
'''

'''
-- 3.	Using sep
The sep parameter lets you specify how to separate elements when printing. In this example, the elements “Never”, “stop”, “learning” will be printed with a comma and a space between them, resulting in “Never, stop, learning”. You can change sep to any string you want as a separator.
'''

print("Never", "stop", "learning", sep=", ")

'''
Output:
Never, stop, learning
'''

'''
-- 4.	Using end
The end parameter changes what gets printed at the end of the print call. Instead of printing each message on a new line, end="" ensures that “Never” and “stop learning” are printed on the same line, resulting in “Never stop learning.” By default, end is a newline ("\n"), which makes each print call start on a new line.
'''

print("Never", end=" ")
print("stop learning")

'''
Output:
Never stop learning
'''
'''
-- 5.	Printing Variables
You can use print to display the value of variables. In this example, it will print “Phrase: Never stop learning” and “Author: Platzi.” This is useful for debugging and seeing variable values at different points in your program.
'''

phrase = "Never stop learning"
author = "Platzi"
print("Phrase:", phrase, "Author:", author)

'''
Output:
Phrase: Never stop learning Author: Platzi
'''

'''
-- 6.	Using f-strings for Formatting
F-strings allow you to insert expressions within text strings. By adding an f before the string, you can include variables directly within braces {}. In this example, phrase and author are inserted into the string, resulting in “Phrase: Never stop learning, Author: Platzi.” This makes the code more readable and easy to write.
'''


phrase = "Never stop learning"
author = "Platzi"
print(f"Phrase: {phrase}, Author: {author}")

'''
Output:
Phrase: Never stop learning, Author: Platzi
'''

'''
-- 7.	Using format for Formatting
The format method is another way to insert values into text strings. Using {} as placeholders, you can pass the values you want to insert as arguments to format. In this example, it will print “Phrase: Never stop learning, Author: Platzi.” This is a flexible and powerful way to format strings, though f-strings are more concise.
'''

phrase = "Never stop learning"
author = "Platzi"
print("Phrase: {}, Author: {}".format(phrase, author))

'''
Output:
Phrase: Never stop learning, Author: Platzi
'''

'''
-- 8.	Printing with Specific Format
You can control the format of numbers when printing. In this example, :.2f indicates that the number should be displayed with two decimal places. Thus, it will print “Value: 3.14,” rounding the number to two decimal places. This is especially useful when working with numerical data and needing a specific format.
'''

value = 3.14159
print("Value: {:.2f}".format(value))

'''
Output:
Value: 3.14
'''

'''
-- 9.	Line Breaks and Special Characters
Line breaks in Python are indicated with the escape sequence \n. For example, to print “Hello\nworld,” which will appear on two lines:
'''

print("Hello\nworld")

'''
Output:
Hello
world
'''

'''
To print a string that contains single or double quotes, you need to use escape sequences to avoid confusion with Python’s syntax. For example, to print the phrase “Hello I am ‘Carli’”:
'''

print('Hello I am \'Carli\'')

'''
Output:
Hello I am 'Carli'
'''

'''
If you need to print a file path on Windows, which includes backslashes, you’ll also need to use escape sequences to prevent Python from interpreting backslashes as part of escape sequences. For example:
'''

print("The file path is: C:\\Users\\User\\Desktop\\file.txt")

'''
Output:
The file path is: C:\Users\User\Desktop\file.txt
'''

'''
In Python, these escape sequences allow you to handle special characters and structure text output as needed, ensuring the output is formatted correctly in the console or any other medium where it’s printed.

With these examples and additional explanations, you’ll have a more complete understanding of how to handle line breaks and special characters in Python when using the print function.
'''

