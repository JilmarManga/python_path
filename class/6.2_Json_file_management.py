import json

#reading of the file
with open('Resources/python-JSON/products.json', mode='r') as file:
    products = json.load(file) #variable 'productos' storages the file that used the method "load" "cargar" for reading the file content

#showing the content
for product in products:
    #print(product)
    print(f"Product: {product["name"]}, Price: {product["price"]}")




#adding a new item to the json file

#path of the file
file_path = "Resources/python-JSON/products.json"

#new item to be added, in Json format
new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargeMaster',
    'category': 'Accessories',
    'entry_date': '2025-01-13',
}

#Reading the Json file and storaging on a "products" variable
with open(file_path, mode="r") as file:
    products = json.load(file)

products.append(new_product)

#ading new_product to the Json file
with open(file_path, mode="w") as file:
    json.dump(products, file, indent=4)
