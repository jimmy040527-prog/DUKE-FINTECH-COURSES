# Array Max
1. Open the provided array_max.py file and write the function:
   ```python
   def array_max(array);
   """
   Finds the largest number in the list
   Ignores elements that are not an int or a float

   Args:
      array (list): list of numbers (either float or int)

   Returns:
   Largest number in the list.  None if array is empty
   or if array is not a list.
   """
   ```

2. You may not use the built-in `max()` as part of your solution.  
   You'll also find that it does not work if a list contains incompatible
   types such as ints and strings. That function will work on ints and floats 
   in a list as they are compatible for performing comparisons and arithmetic.

3. We have provided code that will print test cases and your
   function's response for them.  `test.py`
   You can execute `python3 test.py`

4. We presented the built-in function `type()` in the notebook
   "Types,Values,Variables,Names".
   You can test if a variable `a` is `None` with  `a is None`

5. Test your code.  You should get 99, -3, 425, None, None, None, 45.2  
   for the 7 tests provided.

6. Submit `array_max.py`
