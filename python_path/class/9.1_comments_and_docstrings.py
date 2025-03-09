# 1 - Clarity in code and comments.
# 2 - Keep the comments updated.
# 3 - Do not overuse comments.

def calculate_average(numbers):
    """
    _summary_: calculate the average of a list of numbers

    Args:
        numbers (list): A list of integers or float numbers

    Returns:
        Float: Average of the numbers in the list
    """
    return sum(numbers) / len(numbers)

# Printing the resoult of the function
print(calculate_average([1,2,3,4,5]))