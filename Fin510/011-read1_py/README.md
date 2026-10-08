# Python - Memory Trace Diagram

1. Create a file `answer.txt`.
2. Execute the code under the instructions by hand as demonstrated with the
   memory/trace diagrams in class - you'll need to create a diagram.
   Write the output in your `answer.txt` file
3. Take a picture of your diagram.
4. Submit both your `answer.txt` file and your diagram (this can be png/jpg/pdf) for grading

Please note the correct file name to submit.

```python
a = 3
b = 9
while a <= b:
    if a % 2 == 1:
        print("a is", a)
    else:
        print("b is", b)
        for i in range(0, b-a):
            print("a * i + b =", a * i + b)

    a += 1
    b -= 1
```
