
# POO = (Object-Oriented Programming)

class Person: #Best practice is using first capital letter for a class name
    def __init__(self, name, age): # (Constructor) this fucntion defines the constructor, Constructor is a special fucntion of the classes where you can define the main atributes of the object
        self.name = name
        self.age = age

    def greet(self): #The specific function of a class or and object are called "methods"
        print(f"Hi, my name is {self.name} and I am {self.age}")

person1 = Person("Ana", 30) #Creating a new object in a variable
person2 = Person("Luis", 25)

person1.greet() #calling the fucttion (Method) greting with the object "Person1"
person2.greet()

print("____________________________________")

#Creating a bank account

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"{amount} USD has been deposited, current balance is {self.balance} USD")
        else:
            print("It is not possible to deposite, inactive account")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"An amoun of {amount} USD has been withdrawn, Current balance is {self.balance} USD")

    def deactivate(self):
        self.is_active = False
        print(f"The acount has been deactivated")

    def activate(self):
        self.is_active = True
        print(f"The acount has been activated")

#Creating objects
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

#Calling Methods
account1.deposit(200)
account2.deposit(100)
account1.deactivate()
account1.deposit(500)
account1.activate()
account1.deposit(500)


print("____________________________________")


# Library management Exercise

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"The book {self.title} has been borrow")
        else:
            print(f"The book {self.title}, is not available")

    def return_book(self):
        self.available = True
        print(f"The book {self.title}, has been returned")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed.append(book)
        else:
            print(f"The book {self.title} is not available")

    def return_book(self, book):
        if book in self.borrowed:
            book.return_book()
            self.borrowed.remove(book)
        else:
            print(f"The book {book.title} is not in the list of borrowed books")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title} has been added")

    def register_user(self, user):
        self.users.append(user)
        print(f"The user {user.name} has been registered")

    def show_available_books(self):
        print("Available books: ")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")

#creating objects "Books"

book1 = Book("The little prince", "Antonie de Saint-Exupéry")
book2 = Book("1984", "George Orwell")


#Creating onjects "Users"
user1 = User("Carli", "001")
user2 = User("Carli", "001")


#Creating library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Showing books
library.show_available_books()

#Borrowing books
user1.borrow_book(book1)

#Showing available books
library.show_available_books()

#returning books
user1.return_book(book1)

#Showing books
library.show_available_books()


print("____________________________________")


#Inheritance in OOP” (Object-Oriented Programming)

"""In object-oriented programming (OOP) in Python, inheritance is a mechanism where a class (called the child class or subclass) can derive properties and behaviors (attributes and methods) from another class (called the parent class or superclass).

Key Points:
	1.	Reusability:
	•	Child classes reuse and extend the functionality of parent classes, reducing code duplication.
	2.	Hierarchy:
	•	Establishes a relationship between classes, often described as an “is-a” relationship (e.g., a Dog is an Animal).
	3.	Customization:
	•	Child classes can override or extend methods and attributes of the parent class."""

class Vehicle: # Cosntructor of the class Vehicle
    def __init__(self, maker: str, model: str, year: int, price: float):
        # --- Encapsulation --- Variables of intances that contains private information of the object
        self.maker = maker
        self.model = model
        self.year = year
        self.price = price
        self.available = True

    def __str__ (self): #Method used to efine a readable string representation of an object (Magic method, dunder method)
        return f"{self.maker} {self.model} {self.year} - {self.price:,.2f}"

    def sell(self):
        if self.available:
            self.available = False
            return f"The Vehicle {self.maker} {self.model} has been sold"
        else:
            return f"The vehicle {self.maker} {self.model} is not available for sale"

    # --- Abstraction --- Is it just posible access to the variables asigned to the class previously like "available", "maker" or "model" through the methods created to contained them
    def check_availability(self):
        return self.available

    # --- Abstraction ---
    def get_price(self):
        return self.price

    def start_engine(self): #exception
        raise NotImplementedError("This method must be implemented by the subclass")

    def stop_engine(self): #exception
        raise NotImplementedError("This method must be implemented by the subclass")

# --- Inheritance --- the class Car inherits the atributes of the parent class vehicles
class Car(Vehicle):
        # --- Polymorphism --- in Python polymorphism allows different objects to use the same method name but perform different actions, in this case "start_engine" and "stop_engine" where declarated i the parent class Vehicle but its funtionality changes in the subclass Car
        def start_engine(self):
            if not self.available:
                return f"The {self.maker} {self.model}'s engine is running"
            else:
                return f"The car {self.maker} {self.model} is not available"

        # --- Polymorphism ---
        def stop_engine(self):
            if self.available:
                return f"The {self.maker} {self.model} has been stoped"
            else:
                return f"The car {self.maker} {self.model} is not available"

# --- Inheritance ---
class Bike(Vehicle):
        def start_engine(self):
            if not self.available:
                return f"The {self.maker} {self.model}'s is running"
            else:
                return f"The car {self.maker} {self.model} is not available"

        def stop_engine(self):
            if self.available:
                return f"The {self.maker} {self.model} has been stoped"
            else:
                return f"The car {self.maker} {self.model} is not available"

# --- Inheritance ---
class Truck(Vehicle):
        def start_engine(self):
            if not self.available:
                return f"The {self.maker} {self.model}'s engine is running"
            else:
                return f"The truck {self.maker} {self.model} is not available"

        def stop_engine(self):
            if self.available:
                return f"The {self.maker} {self.model} has been stoped"
            else:
                return f"The truck {self.maker} {self.model} is not available"

#Inherited objects

class Customer: # Cosntructor of the class customer
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = [] #List of the vehicles purchased by each customer

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            f"{vehicle.maker} {vehicle.model} is not available"

    def inquire_vehicle(slef, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "Available"
        else:
            availability = "Unavailable"
        print(f"{vehicle.maker} {vehicle.model} is {availability} and its price is {vehicle.price:,.3f}")

class Dealership: #Cosntrctor of the class Dealersihp
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"The vehicle {vehicle.maker} {vehicle.model} has been added to the inventory")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name}'s has been added to the list of customers")

    def show_available_vehicle(self):
        print("Available vehicles in storage")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.maker} {vehicle.model}'s cost is {vehicle.get_price()}")


#Declarating vehicles and customers
car1 = Car("Mazda", "CX-90", 2025, 80000)
bike1 = Bike("Shimano", "T-1000", 2025, 6000)
Truck1 = Truck("Volvo", "FMX", 2025, 150000)

customer1 = Customer("Jilmar")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(Truck1)

#Available vehicles
dealership.show_available_vehicle()

#Cheking cars available
customer1.inquire_vehicle(car1)

#Buy the car
customer1.buy_vehicle(car1)

#Available vehicles
dealership.show_available_vehicle()


# ------ Use of super() in python --------

class Person: #super calss
    def __init__(self, name: str, age: int): #constructor
        #Atributes of the super class
        self.name = name
        self.age = age

    #method of the super class
    def greet(self):
        print("Hi, I'm a person")

class Student(Person): #Subclass
    def __init__(self, name: str, age: int, student_id: int): #As we are calling the atributes of the super class we must add the constructor of the super class, we must use the same variables of the super class here but we can also add somo moere as needed
        super().__init__(name, age) #Function "Super() allows to work with the atributes and methods of the super class into the subclass"
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello my name is {self.name} and my Student ID is {self.student_id}")

student = Student("Jilmar", 30, 210520)
student.greet()