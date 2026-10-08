# MyClock24

Implement a class named `MyClock24` that represents a 24-hour hour clock.

Define `MyClock24` in a file named `clock.py`.

This class should have a single initializer that takes hours, minutes, and 
seconds. Validate that those values are within acceptable ranges.  If not, 
you should raise a `ValueError`.

We have implemented a `pytest` test file in `test_clock.py`.  You can run the 
tests in this file with -
```bash
pytest test_clock.py 
```

You need to implement all of the behavior defined below:
1. Expose a @property for hours, minutes, seconds. 
2. You may implement additional @property and @property_name.setter  methods as needed
3. Implement a `tick()` method that advances the clock by one second.
4. Implement a `__str__()` method that prints the time in this format: HH:MM:SS
5. Implement a `__repr__()` method that prints out the hour, minute, and second
   attributes as a dictionary literal.
6. Implement the magic methods for `eq`, `ne`, `ge`, `gt`, `le`, `lt`. Use the
   comparison of the full time for these methods.
7. Implement the magic methods for `add` and `sub`. These functions accept 
   another `MyClock24` object as the second parameter or an `int` that 
   represents the number of ticks to move the clock forward or back.

Note: If the time goes outside the range of 00:00:00 to 23:59:59, then the time 
should roll over / roll back as appropriate.

How you track the internal state of the clock is your implementation detail.

Once your `MyClock24` passes the test cases, submit your work(`clock.py`) for grading.
