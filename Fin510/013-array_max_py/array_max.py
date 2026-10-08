def array_max(array):
    """
    Finds the largest number in the list.
    Ignores elements that are not an int or a float

    Args:
        array (list): list of numbers (either float or int)

    Returns:
    Largest number in the list.  None if array is empty
    or if array is not a list.
    """
    my_max = - float('inf')
    for i in array:
        if isinstance(i, (int, float)):
            if i > my_max:
                my_max = i
    return my_max if my_max != - float('inf') else None
