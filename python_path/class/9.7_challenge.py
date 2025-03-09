"""
1- You will recebe a list of dictionaries, each will have the keys: "name", "age", "salary".
2- you have to create a function that returns a list of employeees earning more than a s[ecefic salary threshold.
"""

"""import random
import string


# Genera te a random name
def random_name(lengh=5):
    return "".join(random.choices(string.ascii_letters, k=lengh)).capitalize()

#generate the list of dictionaries

people = [
    {
        "name": random_name(random.randint(4, 8)),
        "age": random.randint(20, 60 ),
        "salary": random.randint(3000, 12000)
    }
    for _ in range(100)
]

people
print(people)"""


employees = [
    {"name": "Alice", "age": 30, "salary": 60000},
    {"name": "Bob", "age": 25, "salary": 48000},
    {"name": "Charlie", "age": 35, "salary": 72000},
    {"name": "Diana", "age": 28, "salary": 51000},
    {"name": "Eve", "age": 40, "salary": 90000},
]

def filter_high_salary_employees(salary_threshold):
    """
    Filters and returns employees earning mopre than the specific salary threshold.
    """
    return [emp for emp in employees if emp["salary"] > salary_threshold]

if __name__ == "__main__":
    try:
        threshold = 1000
        high_earners = filter_high_salary_employees(threshold)

        print(f"Employees earning more than ${threshold}:")
        for emp in high_earners:
            print(f"- {emp['name']} (Age: {emp['age']}, Salary: ${emp['salary']})")
    except Exception as e:
        print(f"An error occurred: {e}")