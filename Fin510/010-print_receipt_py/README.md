# Print Receipt

Write a function with the following declaration - 
```python
def print_receipt(subtotal, tax_rate, tip_rate):
```

That prints the following:
```text
Subtotal: $     10.00
     Tax: $      0.50
     Tip: $      2.00
           ==========
   Total: $     12.50
```
with the call: `print_receipt(10.00, .05, .2)`
Use formatting for all of the numbers and equal signs.

Within the United States, we typically pay taxes on most purchases.
We also "tip" waitstaff for their service at restaurants.  Both taxes and
tips are typically computed as a percentage of the initial bill (subtotal).

So that we can automatically grade programs, follow these conditions:
1. The Python file must be named `print_bill.py`. 
   Use the function declaration provided above
2. We will directly call your function and evaluate the result.
3. You should not have any input within your `print_bill.py` file.
4. Taxes are computed by multiplying the tax_rate and subtotal. 
   Similarly, tips are computed by multiplying the tip_rate and subtotal.
5. You must provide a docstring so others can understand your function.

To test your program, you may use `test.py`.
This file will make a sample call to your function.  You should add
additional calls to further evaluate your function.

## Sample Execution
```bash
$ python3 test.py
Subtotal: $     10.00
     Tax: $      0.50
     Tip: $      2.00
           ==========
   Total: $     12.50
```

## test.py
```python
from print_bill import print_receipt

print_receipt(10.00, .05, .2)
```
