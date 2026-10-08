# Paycheck

In this programming assignment, you will write a program 
that computes a simple weekly paycheck for an individual. 

Prompt the user to enter the number of hours worked and the pay rate. 
If an individual works over 40 hours, then the individual is paid at 1.5 
times the hourly rate for the hours worked over 40. Print the initial 
total. Of course, the government taxes the individual's pay. Assume the 
tax rate is 20%. Print the amount withheld for taxes. Then print the 
net amount to be paid to the individual.

So that we can automatically grade programs, you must follow these
specific conditions:
1. The Python file must be named "paycheck.py". 
2. You need to use the following as prompts within the input functions:
   "How many hours did the employee work?"
   "What is the employee's pay rate?"
3. Follow the print style in the last line of paycheck.py
4. Use the following strings to label the values:
   ```python
   "Total pay:"
   "Taxes:"
   "Net pay:"
   ```
5. You may assume we will provide valid input (positive numbers)
6. You can use the following code as a sample (must be modified) to print
   ```python
   a = 5                   # sample code only to demonstrate how to print
   print("Test value:",a)  # Copy this line and modify the label and variable
                           # to display results
   ```

You can execute your program with
```bash
python3 paycheck.py
```

Sample Executions:
```bash
$ python3 paycheck.py
How many hours did the employee work?55
What is the employees pay rate?100
Total pay: 6250.0
Taxes: 1250.0
Net pay: 5000.0
```

```bash
$ python3 paycheck.py
How many hours did the employee work?38.25
What is the employees pay rate?7.75
Total pay: 296.4375
Taxes: 59.2875
Net pay: 237.15
```