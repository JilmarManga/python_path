# Object-oriented programming (OOP)

'''
Summary

What is Metaprogramming in Python?

As we delve into object-oriented programming, we encounter a fascinating concept: metaprogramming. This approach not only allows us to create classes and objects but also provides advanced tools to optimize and control instance creation. From using the __init__ method to handling __new__, metaprogramming opens up a range of possibilities for developing more flexible and dynamic software.
'''
#--------------------------------------------------------
'''
How Are __init__ and __new__ Applied in a Python Class?

How Does the __init__ Method Work?

When we create a class in Python, __init__ is one of the first concepts we learn. Its main function is to initialize an instance’s attributes, setting the initial state of an object:
'''

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        print(f"Initializing with factor {factor}")

'''
In this example, __init__ takes a factor parameter and assigns it as an attribute of the object. It also prints a message confirming the initialization, which is useful for tracking how instances are configured.
'''

#--------------------------------------------------------

'''
What Does the Special __new__ Method Do?

Unlike __init__, the __new__ method is responsible for creating a new instance of a class. This method is called before __init__ and is crucial when stricter control over instantiation is needed:
'''

class Multiplier:
    def __new__(cls, factor):
        print(f"Creating instance with factor {factor}")
        instance = super(Multiplier, cls).__new__(cls)
        return instance

'''
Here, __new__ prints a message indicating the start of object creation. It then uses super() to call the highest constructor in the class hierarchy, ensuring the object is properly initialized before passing it to __init__.
'''

#--------------------------------------------------------

'''
How to Combine These Methods in a Real Project?

Suppose you have a project where you need to dynamically generate multipliers. Using both __new__ and __init__ together can give you the control and flexibility needed:
'''
class Multiplier:
    def __new__(cls, factor):
        print(f"Creating instance with factor {factor}")
        instance = super(Multiplier, cls).__new__(cls)
        return instance

    def __init__(self, factor):
        self.factor = factor
        print(f"Initializing with factor {factor}")

# Creating an instance of Multiplier
multi = Multiplier(5)

'''
When running this code, you get an execution flow where __new__ first creates the instance, and then __init__ initializes it. The printed messages help you track the entire creation process, ensuring everything works as expected.
'''

#--------------------------------------------------------

'''
Practical Tips for Using Metaprogramming

Here are some recommendations to make the most of these concepts in your projects:
	•	Assess the project’s complexity: Use metaprogramming only when advanced flexibility and control are required. For simpler projects, basic class implementation is sufficient.
	•	Maintain a logical order: As shown in the examples, __new__ should always precede __init__ to follow the correct instance creation flow.
	•	Document your code: Since metaprogramming can be challenging to understand at first glance, keeping clear documentation is essential for easier maintenance and collaboration.

Metaprogramming in Python is a powerful tool that, when properly understood and applied, can significantly improve the quality and performance of your projects. Keep exploring and experimenting to unlock everything you can achieve with these methods! 🚀
'''

#--------------------------------------------------------

class MultiplierFactory:

    def __new__(cls, factor: int):
        print(f"creating instance with factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)

    def __init__(self, factor: int):
        print(f"Initializing with factor {factor}")
        self.factor = factor

    def __call__(self, number: int) -> int:
        return number * self.factor

multiplier = MultiplierFactory(5)

result = multiplier(10)
print(result)