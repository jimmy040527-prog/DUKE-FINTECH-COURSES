# Read Recursion - Python

1. Create a file `answer.txt`.
2. Execute the code under the instructions (also in `test.py`) by hand as 
   demonstrated with the memory/trace diagrams in class - you'll need to 
   create a diagram.  Write the output in your `answer.txt` file
3. Take a picture of your diagram.
4. Submit both your `answer.txt` file and your diagram (this can be png/jpg/pdf)
   for grading

```python
def printDigits(x):
    print("printDigits called with {:d}".format(x))
    if x == 0:
        print("0",end="")
    elif (x < 0):
        print("-",end="")
        printDigits(-x)
    else:
        a = x // 10
        b = x % 10
        print("a={:d}, b={:d}".format(a,b))
        if a != 0:
            printDigits(a)

        print(b,end="")

printDigits(297)
print()
```
