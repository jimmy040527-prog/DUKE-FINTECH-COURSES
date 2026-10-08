# Budget Tracking  Evaluative Assignment

In this assignment, you will write a program to process budget data for multiple
departments within an organization.

As an evaluative assignment, your work must be your own. Your submission
of the assignment implies you have read and followed the assignment
rules at the bottom of this page.

Several steps exist for this assignment:
1. Load and process department information file
2. Print department information
3. Load and process the expense information file
4. Determine which departments are over budget
5. Print over-budget departments to the console
6. Determine which departments require budget alerts
7. Save the alert information to a file
8. Determine which department had the largest budget variance
9. Print the largest variance to the console
10. Based upon actual expenses, compute the efficiency metric (cost per employee)
    and display the results by that metric in descending order.

## Department Information File

Before you start, take a look at `departments.txt`. This file contains multiple
lines (one for each department), describing the department name, allocated 
budget, and number of employees. Each department will have at least 1 employee.

For example, the first line is:

```
Marketing:150000:12
--------- ------ --
  \        \     \  Number of employees in this department
   \        \     --------------------------------------------
    \        \ Allocated budget for this department ($)
     \        ----------------------------------------
      \  Department name
       --------------------
```

If you look through the rest of the file, you will see that each line contains 
the same format.

There is also a simpler file `simple_departments.txt` with three departments to 
help you test (so it is easier to figure out the right answer).

## Expense Information File

Next, take a look at `expenses.txt`. This file contains multiple lines (one for
each department), describing the actual expenses incurred by each department.
There is no guarantee that the ordering of the departments matches the first 
file. However, the department names will all be present and match the first 
file exactly.

```
Marketing:147500
--------- ------
 \        \  Actual expenses for this department ($)
  \        ------------------------------------
   \  Department name
    ----------------
```

As with `simple_separtments.txt`, there is a simpler version with just four 
departments: `simple_expenses.txt`

## Functions to Write

```python
def parse_department_information(filename):
    """
    Opens the department information file named in filename, loads all of the 
    values, placing them in a single data structure. Returns that data 
    structure. You may create nested data structures.
        
    Ignore any lines that are empty or have and invalid data.
    
    If the file cannot be opened, print an error message and exit with status code 2.
    """

def print_department_information(dept_info):
    """
    For the dept_info data structure (produced as a result),  
    print all departments in alphabetical order using the string:
    "{}: Budget - ${:,d}, Employees: {:d}"
    """

def parse_expense_information(filename):
    """
    Opens the expense information file and returns the information 
    in a data structure

    Ignore any lines that are empty or have and invalid data.
    
    If the file cannot be opened, print an error message and exit with status code 2.
    """

def calculate_budget_variance(dept_info, expense_info):
    """
    Calculates and returns a dictionary containing budget variance information
    for each department. Variance is calculated as: 
    (actual_expenses - budget) / budget * 100
    
    Positive variance means over budget, negative variance means under budget.
    Returns a dictionary where keys are department names and values are 
    variance percentages.
    """

def determine_over_budget_departments(dept_info, expense_info):
    """
    Determines which departments have exceeded their allocated budget.
    Returns a list of department names that are over budget.
    """

def print_over_budget_departments(over_budget_list, dept_info, expense_info):
    """
    Prints the over-budget departments. For each department, print:
    "{} is over budget by ${:,d} ({:.2f}% over)"
    Sort the departments alphabetically.
    
    If no departments are over budget, print "All departments are within budget."
    """

def determine_budget_alerts(dept_info, expense_info):
    """
    Produces a list of strings, where each string represents information
    about a department that requires a budget alert. Budget alerts are required 
    when a department is within +/- 5% of their budget limit (95% to 105% of budget).
    
    Only include departments that require alerts in the result. For each department
    that requires an alert, include a line of the form:
    "{} requires budget monitoring (at {:.2f}% of allocated budget)".
    """

def save_budget_alerts(alert_list):
    """
    Saves each entry of the list to a file named "budget_alerts.txt". The
    entries must be printed in alphabetical order by department name.
    """

def determine_largest_variance(dept_info, expense_info):
    """
    Determines which department had the largest budget variance (either positive
    or negative).
    
    Returns a string with the following format:
    "{} had the largest variance at {:.2f}% ({} budget)"
    
    where the first {} should be the name of the department, {:.2f} should be the 
    absolute percentage variance, and the third {} should be either "over" or "under".
    For example, it might return:
    "IT had the largest variance at 15.30% (over budget)"
    
    Returns None if no departments have a budget variance or if there is not a 
    single department with the largest variance.
    """

def calculate_efficiency_metrics(dept_info, expense_info):
    """
    Calculates expense per employee for each department.
    Returns a dictionary where keys are department names and values are 
    expense per employee (actual_expenses / number_of_employees).
    """

def process(dept_info_filename, expense_info_filename):
    """
    Implements the "Several steps exist for this assignment" section:
    1. Load and process department information
    2. Print department information
    3. Load and process expense information
    4. Determine and print over-budget departments
    5. Determine budget alerts and save to file
    6. Determine and print largest variance
    7. Calculate and display efficiency metrics
    """
```

## Main Section

You should also include a "main section" that validates the number of 
command-line arguments (see the sample execution for the expected argument). 
If the number is wrong, print an error message and exit
with the value of 101. Then call `process(dept_info_filename, expense_info_filename)`.

When you are satisfied with your testing, submit your assignment for grading. 
Your work should be in `budget.py`.

## Sample Execution

When your program runs successfully, it should produce the following output:
```
% python budget.py simple_departments.txt simple_expenses.txt
HR: Budget - $75,000, Employees: 5
IT: Budget - $200,000, Employees: 8
Marketing: Budget - $150,000, Employees: 12
IT is over budget by $25,000 (12.50% over)
IT had the largest variance at 12.50% (over budget)
IT: $28,125.00 per employee
HR: $14,200.00 per employee
Marketing: $12,291.67 per employee
```
The file `budget_alerts.txt` will have the following contents:
```
Marketing requires budget monitoring (at 98.33% of allocated budget)
```

## Assignment Details
1. In a file algorithm.md, perform the following work:
   1. Have a top-level heading (i.e., the lines starts with just "#") with a
      label of "Budget Tracker".  You may have an optional description under
      that heading.
   2. A second-level heading with a label of "Determine Largest Variance"
   3. Write an algorithm (pseudocode) to implement the `determine_largest_variance`
      function. You need to list at least three steps as an ordered list.
   4. Have another second-level heading with a label of "Tests"
   5. Describe at least three possible test cases for `determine_largest_variance`. 
2. Write `budget.py` to implement the necessary code for this assignment.
3. Create test files as needed to validate your changes locally.
4. Review `CodeReviewRubric.pdf` and make any changes you feel are necessary
   to your `budget.py` file.

## Notes
- Don't try to complete all of this at once. Get small pieces of the code working
  and validated, then continue to add more functionality.
- Unlike previous assignments, you will not receive the complete score until after
  the assignment deadline (which is a hard deadline, with any late assignments 
  receiving a maximum score of 70%).
- The "pregrader" tests the provided files and is worth 75% of the grade.
- 5% of the grade is a manual code review
- 10% of the score is `algorithm.md`. While this is automatically graded, the 
  file will be reviewed as part of the manual code review and adjusted if
  necessary.

## Assignment Rules
- Your work must be your own!
- You may NOT consult with other students about the following:
  - high level approaches,
  - how to implement your algorithm, or
  - how to debug your code.
  
  Basically, you may not discuss anything particular to this assignment.

- You may NOT look at another student's code, nor show your code to
  anyone else.
- You are responsible for keeping your code private.
- You may not look for solutions to this or similar problems online.
- You may not use code from any other source.
- You may not use any AI assistive technology, including Qubit.

- You MAY consult any of the course Jupyter notebooks
- You MAY consult any Python book on the O'Reilly Learning Platform
- You MAY consult any Python documentation on https://www.python.org/doc/
- You MAY consult notes you wrote in your notebook.
- You MAY consult the man pages.
- You MAY ask the professor or TAs for clarification on the assignment.
