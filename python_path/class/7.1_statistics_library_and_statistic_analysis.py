import statistics
import csv


# Reading the monthly sales data from a CSV file

monthly_sales = {}
with open("Resources/python-CSV/monthly_sales.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row["month"]
        sales = int(row["sales"])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)


print('\n\n\n mean method ---------------------------------')

# using mean method
mean_sales = statistics.mean(sales)
print(f"The mean sales is: {mean_sales}")


print('\n\n\n mode method ---------------------------------')

# using mean method = moda
mode_sales = statistics.mode(sales)
print(f"The mode sales is: {mode_sales}")


print('\n\n\n standar deviation method ---------------------------------')

# using standar deviation method
stdev_sales = statistics.stdev(sales)
print(f"The mode sales is: {stdev_sales}")


print('\n\n\n variance method ---------------------------------')

# using variance method
variance_sales = statistics.variance(sales)
print(f"The mode sales is: {variance_sales}")


print('\n\n\n maximun and minimun methods ---------------------------------')

max_sales = max(sales)
print(f"maximun sales were: {max_sales}")

min_sales = min(sales)
print(f"minimun sales were: {max_sales}")

# getting the range of slaes from max to min
range_sales = max_sales - min_sales
print(f"Range of sales: {range_sales}")
