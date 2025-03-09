# It's not necesssary to import any library because collections and enumerations are built-in libraries in Python.

print('\n\n\n defaultdict ---------------------------------')

from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    # Crerate a dictionary with a default value of 0
    count_products = defaultdict(int)
    for product in orders:
        count_products[product] += 1
    return count_products

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)


print('\n\n\n Counter ---------------------------------')


from collections import Counter

def count_sales(products: list[str]) -> Counter:
    # using Counter to get to know how many of each product is sold
    return Counter(products)

sales = ['laptop', 'smartphone', 'laptop', 'tablet', 'smartphone']
result = count_sales(sales)
print(result)


print('\n\n\n Manage Delivery Queu ---------------------------------')

from collections import deque

def manage_delivery_queue() -> deque:
    # Create a queue for managing delivery orders
    delivery_queue = deque(["order1", "order2", "order3", "order4", "order5"])
    # Add a new order to the queue
    delivery_queue.append("order6")
    # Remove the first order from the queue
    delivery_queue.popleft()
    # Add a new order to the beggining of the queue
    delivery_queue.appendleft("order0")
    # Remove the last order from the queue
    delivery_queue.pop()
    return delivery_queue

queue = manage_delivery_queue()
print(queue)


print('\n\n\n Manage Delivery Queu ---------------------------------')

from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4

def check_order_status(status: OrderStatus) -> str:
    # Check the status of the order
    if status == OrderStatus.PENDING:
        return "Order is pending"
    elif status == OrderStatus.PROCESSING:
        return "Order is processing"
    elif status == OrderStatus.SHIPPED:
        return "Order is shipped"
    elif status == OrderStatus.DELIVERED:
        return "Order is delivered"

print(check_order_status(OrderStatus.PENDING))
print(check_order_status(OrderStatus.SHIPPED))
print(check_order_status(OrderStatus.DELIVERED))
print(check_order_status(OrderStatus.PROCESSING))