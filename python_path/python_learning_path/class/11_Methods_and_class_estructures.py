# Mahgic methods: Add inter functionalities to the class

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Magic-method string: This method is used to define how is shoed an object is displayed when convert to string to make it user-friendly
    def __str__(self) -> str:
        return f'Person: {self.name}, {self.age} years old'

    # Magic-method rept: Workas as an official representation of the object (details ob the object)
    def __repr__(self) -> str:
        return f'Person(name: {self.name}, age: {self.age})'

    #Magic-method eq: Compare two objects using the == operator
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

    #Magic-method lt: Compare two objects using the < operator
    def __lt__(self, other) -> bool:
        return self.age < other.age

    #Magic-method add: Add two objects using the + operator
    def __add__(self, other):
        return self.age + other.age


# Create a person instance
p1 = Person('John', 28)
p2 = Person('Jane', 25)
p3 = Person('Doe', 30)
p4 = Person('John', 28)

# def __str__(self) example
print(f'result magic-method str:', p1)  # Person: John, 28 years old

# def __repr__(self) example
print(f'result magic-method repr:', repr(p2))  # Person(name: Jane, age: 25)

# def __eq__(self) example
print(f'result magic-method eq:', p1 == p2)  # False
print(f'result magic-method eq:', p1 == p4)  # True

# def __lt__(self) example
print(f'result magic-method lt:', p1 < p2)  # False
print(f'result magic-method lt:', p1 < p3)  # True

# def __add__(self) example
print(f'result magic-method add:', p1 + p2)  # 53
