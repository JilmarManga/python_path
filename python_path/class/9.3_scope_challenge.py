"""Create in python a program using 2 functions the first one will get this list of dictionaries:
[
        {"name": "Alice", "age": 30, "salary": 60000},
        {"name": "Bob", "age": 25, "salary": 48000},
        {"name": "Charlie", "age": 35, "salary": 72000},
        {"name": "Diana", "age": 28, "salary": 51000},
        {"name": "Eve", "age": 40, "salary": 90000},
    ]

    The second one will return a list of employers who earn more than an specific salary... the code must be written with high good practices, it must be efficient  and it must contain comments and manage errors """

# Chat GPT solution:

# Global variable to store the list of employees
employees = [
    {"name": "Alice", "age": 30, "salary": 60000},
    {"name": "Bob", "age": 25, "salary": 48000},
    {"name": "Charlie", "age": 35, "salary": 72000},
    {"name": "Diana", "age": 28, "salary": 51000},
    {"name": "Eve", "age": 40, "salary": 90000},
]


def filter_high_salary_employees(salary_threshold):
    """
    Filters and returns employees earning more than the specified salary threshold.
    """
    return [emp for emp in employees if emp["salary"] > salary_threshold]


if __name__ == "__main__":
    try:
        threshold = 50000
        high_earners = filter_high_salary_employees(threshold)

        print(f"Employees earning more than ${threshold}:")
        for emp in high_earners:
            print(f"- {emp['name']} (Age: {emp['age']}, Salary: ${emp['salary']})")
    except Exception as e:
        print(f"An error occurred: {e}")