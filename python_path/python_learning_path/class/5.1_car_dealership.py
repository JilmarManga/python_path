# My solution

class Car:
    def __init__(self, maker: str, model: str, year: int, price: float):
        self.maker = maker
        self.model = model
        self.year = year
        self.price = price

    def __str__ (self): #Method used to efine a readable string representation of an object (Magic method, dunder method)
        return f"{self.maker} {self.model} {self.year} - {self.price:,.2f}"


class Inventory:
    def __init__(self):
        self.cars = [] #Create a dicctionary where the cars are goint to be added

    def add_car(self, car: Car):
        self.cars.append(car) #Added the car to a dictionary of cars

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            return car
        else:
            raise ValueError("Car not found in inventory")

    def list_cars(self):
        return self.cars

    def find_car_by_make_model(self, maker: str, model: str):
        return [car for car in self.cars if car.maker == maker and car.model == model]


class CarDealership: #constructor function for managing the Car Delaership operation
    def __init__(self, name: str):
        self.name = name
        self.inventory = Inventory()
        self.sold_cars = []

    def buy_car(self, maker: str, model: str, year: int, price: float):
        car = Car(maker, model, year, price)
        self.inventory.add_car(car)
        return f"{car} has been added to inventory"

    def sell_car(self, maker: str, model:str):
        matching_cars = self.inventory.find_car_by_make_model(maker, model)
        if not matching_cars:
            return "Car ç"
        else:
            car_to_sell = matching_cars[0]
            self.inventory.remove_car(car_to_sell)
            self.sold_cars.append(car_to_sell)
            return f"{car_to_sell} has been sold"

    def return_car(self, car: Car):
        self.inventory.add_car(car) #Car returned is been added to the inventory again through the 'add_car' method
        return f"{car} has been returned to inventory"

    def get_price(self, maker: str, model: str):
        cars = self.inventory.find_car_by_make_model(maker, model)
        if not cars:
            return "Price information is not available"
        else:
            return f"The price for {cars[0]} is ${cars[0].price:,.2f}"

    def view_inventory(self):
        cars = self.inventory.list_cars()
        if not cars:
            return "No cars available in inventory"
        else:
            return "\n".join(str(car) for car in cars) #explanation bellow
            """	1.	(str(car) for car in cars):
	•	This is a generator expression that iterates through the cars list.
	•	For each car object in the cars list, it calls the __str__ method of the Car class (or converts the car object to its string representation).
	•	The result is a generator that yields the string representation of each car, one at a time.
	2.	"\n".join(...):
	•	The join method combines all the strings in the generator into a single string.
	•	Each string (representing a car) is joined together with a newline character (\n) as the separator.
	•	This means each car’s details will appear on a new line in the resulting string.
	3.	return:
	•	The method returns the resulting string, which contains a newline-separated list of all cars in the inventory."""

#Example use

if __name__ == "__main__":
    dealership = CarDealership("Elite Auto Sales")

#Create cars intances
    print(dealership.buy_car("Toyota", "Corolla Cross", 2023, 36000))
    print(dealership.buy_car("Mazda", "CX - 90", 2026, 80000))
    print(dealership.buy_car("Range Rover", "Velar", 2028, 100000))

#Show available cars
    print("\nAvailable cars:")
    print(dealership.view_inventory())

#Geting cars prices
    print("\nGet Price:")
    print(dealership.get_price("Toyota", "Corolla Cross"))
    print(dealership.get_price("Mazda", "CX - 90"))

#Selling car
    print("\nSell Car:")
    print(dealership.sell_car("Mazda", "CX - 90"))

#Showing the available cars after the selling
    print("\nAvailable cars after sale:")
    print(dealership.view_inventory())

"""
#Chat GPT

class Car:
    def __init__(self, make: str, model: str, year: int, price: float):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price:,.2f}"


class Inventory:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            return car
        raise ValueError("Car not found in inventory.")

    def list_cars(self):
        return self.cars

    def find_car_by_make_model(self, make: str, model: str):
        return [car for car in self.cars if car.make == make and car.model == model]


class CarDealership:
    def __init__(self, name: str):
        self.name = name
        self.inventory = Inventory()
        self.sold_cars = []

    def buy_car(self, make: str, model: str, year: int, price: float):
        car = Car(make, model, year, price)
        self.inventory.add_car(car)
        return f"{car} has been added to inventory."

    def sell_car(self, make: str, model: str):
        cars = self.inventory.find_car_by_make_model(make, model)
        if not cars:
            return "Car not available for sale."
        car_to_sell = cars[0]
        self.inventory.remove_car(car_to_sell)
        self.sold_cars.append(car_to_sell)
        return f"{car_to_sell} has been sold."

    def return_car(self, car: Car):
        self.inventory.add_car(car)
        return f"{car} has been returned to inventory."

    def get_price(self, make: str, model: str):
        cars = self.inventory.find_car_by_make_model(make, model)
        if not cars:
            return "Price information not available."
        return f"The price for {cars[0]} is ${cars[0].price:,.2f}."

    def view_inventory(self):
        cars = self.inventory.list_cars()
        if not cars:
            return "No cars available in inventory."
        return "\n".join(str(car) for car in cars)


# Example Usage
if __name__ == "__main__":
    dealership = CarDealership("Elite Auto Sales")

    print(dealership.buy_car("Toyota", "Camry", 2022, 25000))
    print(dealership.buy_car("Honda", "Civic", 2021, 22000))

    print("\nAvailable Cars:")
    print(dealership.view_inventory())

    print("\nGet Price:")
    print(dealership.get_price("Toyota", "Camry"))

    print("\nSell Car:")
    print(dealership.sell_car("Toyota", "Camry"))

    print("\nAvailable Cars After Sale:")
    print(dealership.view_inventory())"""