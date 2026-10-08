# Bull Market

For this assignment, you'll write a function that finds the maximum bull market 
in a series of S&P 500 closing prices as determined by the most number of 
days that the market increased.

1. Create a file called bull_market.py and write the function:
   ```python
   def find_longest_period(l):
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
   ```
   
   For example, if the list passed in were
   [ 5475.25, 5480.40, 5474.00, 5501.23, 5510.30, 5518.42, 5512.41, 5514.92, 5517.76, 5522.44],
   this function would return [5474.00, 5501.23, 5510.30, 5518.42]

2. Create a file "test_bull_market.py" that contains at least three pytest
   functions that test your program.

3. Submit  `bull_market.py` and `test_bull_market.py`

**Hints**

1. Can you abstract a complex step into a simple function?
2. The `TypeError` will occur with the right test case; write that test case.