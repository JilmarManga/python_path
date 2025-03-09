'''

*** Operator Overloading in Python ***

-- 1. What is Operator Overloading?
By default, operators like + and == only work with predefined data types (numbers, strings, lists, etc.). However, with operator overloading, we can modify how these operators behave with our custom classes.

Example: Overloading + Operator

Imagine a Vector class where we want to sum two vectors using +. We achieve this using the magic method __add__:

'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2 # overloaded + operator
print(v3)  # Output: Vector(6, 4)

'''
Here, __add__ defines how two Vector objects should be summed, creating a new vector with the sum of their components.
'''

print('\n\n\ ---------------------------------')

'''
-- 2. Overloading Comparison Operators (==, <, >)
Overloading is not limited to arithmetic operators; we can also redefine comparison operators to compare objects based on custom attributes.

Example: Overloading == for Object Comparison
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload the == operator
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

p1 = Person('John', 28)
p2 = Person('Jane', 25)
p3 = Person('John', 28)

print(p1 == p2) # Output = False
print(p1 == p3) # Output = True

'''
Here, __eq__ allows the == operator to compare two Person objects based on their name and age attributes.
'''

print('\n\n\ ---------------------------------')


'''
-- 3. Overloading Other Operators (<, -, *)

Example: Overloading < (Less Than Operator)
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload the < operator
    def __lt__(self, other):
        return self.age < other.age

p1 = Person('John', 28)
p2 = Person('Jane', 25)

print(p1 < p2) # Output = False

'''
Here, __lt__ allows the < operator to compare two Person objects based on age.
'''


'''
-- 4. Best Practices for Operator Overloading:

	• Use overloading when it makes sense: Don’t overload operators unnecessarily. Use it only when it makes intuitive sense.

	• Maintain consistency: If you overload +, ensure it behaves as expected (e.g., summing components in a Vector class).

	• Document behavior: Overloaded operators can make code cleaner, but it’s important to document how they behave, especially if their functionality isn’t obvious.
'''


'''
-- 5. Practical Exercise: Overloading + in a Fraction Class:

- Objective: Implement a Fraction class that allows adding fractions using +.
- Requirements:
	•	The class should have numerator and denominator.
	•	The + operator should return the result in simplified form.
'''

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other_fraction):
        new_num = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_den = self.denominator * other_fraction.denominator
        common_divisor = gcd(new_num, new_den)
        return Fraction(new_num // common_divisor, new_den // common_divisor)

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

f3 = f1 + f2  # Fraction addition
print(f3)  # Output: 3/4

'''
This example shows how to redefine + to intuitively add fractions.
'''


'''
Conclusion:

Congratulations on completing this class on Operator Overloading in Python! You now understand how to customize operator behavior in your custom classes, allowing for more intuitive, clean, and powerful code.

By mastering operator overloading, you’ve unlocked a new level of flexibility in Python. Now, it’s time to apply what you’ve learned—experiment with your own classes and operators! 🚀
'''