def compute_average(items):
    """
    Computes the average of list, ignoring any entries that 
    are not numbers (floats or ints)

    Args:
    l(list): list of items to compute the average
 
    returns:
    average of the numbers in the list
    
    raises:
    ValueError if the argument is not a list or if the list does not contain any numbers
    """
    # TODO: Implement function
    if not isinstance(items, list):
        raise ValueError

    total = 0
    count = 0

    for item in items:
        if isinstance(item, (float, int)):
            total += item
            count += 1

    if count == 0:
        raise ValueError

    return total / count