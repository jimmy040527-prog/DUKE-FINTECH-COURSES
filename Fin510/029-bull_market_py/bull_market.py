def find_longest_period(prices):
    """
    find_longest_period returns the longest series of closing prices in
    which the prices continually rose (as determined by the number of days).
    If two more more series have the same number of days, return the first
    series found.
        
    Args:
        l(list): list of daily closing prices

    Returns:
    a list containing the series (e.g., part of the original list) that 
    has the closing stock prices in the order in which they appeared in the 
    original list 

    Raises:
    TypeError if the list contains an item that is not arithmetically 
    compatible with ints and floats
    """
    if not prices:
        return []
    for i in prices:
        if not isinstance(i, (int, float)):
            raise TypeError
    res, cur = [prices[0]], [prices[0]]
    n = len(prices)
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            cur.append(prices[i])
        else:
            cur = [prices[i]]
        if len(res) < len(cur):
            res = cur
    return res

    