#import library
import csv

#Reading file
'''with open('Resources/python-CSV/products.csv', mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)'''


#Showing information by columns
'''with open('Resources/python-CSV/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Product: {row['name']}, Price: {row['price']}")'''


#Adding a new line to the file

'''new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargeMaster',
    'category': 'Accessories',
    'entry_date': '2025-01-13',
}

with open('Resources/python-CSV/products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)'''


#Creating a new file, copiying data from other file and addding information (new column)

file_path = 'Resources/python-CSV/products.csv' #Path of the existing file
updated_file_path = 'Resources/python-CSV/products_updated.csv' #path of the new file

with open('Resources/python-CSV/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtaining the names of the existing columns
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames= fieldnames)
        csv_writer.writeheader() #Writing the headers

        for row in csv_reader:
            #Getting the total value by multipliying 'price' by 'quantity' and storaging them on a new column called 'total_value'
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)