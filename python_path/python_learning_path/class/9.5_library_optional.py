# Use of the library optional

from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Searches for an employee ID in a list of IDs and returns the value if it exists.

    Parameters:
    employee_ids (list[int]): List of employee IDs.
    employee_id (int): ID to search for.

    Returns:
    Optional[int]: The found ID or None if it does not exist in the list.
    """
    if employee_id in employee_ids:
        return employee_id
    return None