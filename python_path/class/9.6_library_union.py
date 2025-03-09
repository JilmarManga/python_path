# Use of the library union

from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Processes a salary that can be an integer or a float and returns it as a float.

    Parameters:
    salary (Union[int, float]): A salary that can be an integer or a float.

    Returns:
    float: The salary converted to a float.
    """
    return float(salary)