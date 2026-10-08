import sys


def parse_department_information(filename):
    """
    Opens the department information file named in filename, loads all of the 
    values, placing them in a single data structure. Returns that data 
    structure. You may create nested data structures.
        
    Ignore any lines that are empty or have and invalid data.
    
    If the file cannot be opened, print an error message and exit with status code 2.
    """
    data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
            # split by :
                line = line.split(":", 2)
                if len(line) != 3:
                    continue
                name, budget, number = line
                name = name.strip()
                budget = budget.strip()
                number = number.strip()
                if not name or not budget.isdigit() or not number.isdigit():
                    continue
                data[name] = [budget, number]
    except OSError:
        print("File cannot be opened", file=sys.stderr)
        sys.exit(2)
    return data
        

def print_department_information(dept_info):
    """
    For the dept_info data structure (produced as a result),  
    print all departments in alphabetical order using the string:
    "{}: Budget - ${:,d}, Employees: {:d}"
    """
    for name in sorted(dept_info.keys()):
        Budget = int(dept_info[name][0])
        Employees = int(dept_info[name][1])
        print(f"{name}: Budget - ${Budget:,d}, Employees: {Employees:d}")


def parse_expense_information(filename):
    """
    Opens the expense information file and returns the information 
    in a data structure.
    
    Ignore any lines that are empty or have and invalid data.
    
    If the file cannot be opened, print an error message and exit with status code 2.
    """
    data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
            # split by :
                line = line.split(":", 1)
                if len(line) != 2:
                    continue
                name, expense = line
                name = name.strip()
                expense = expense.strip()
                if not name or not expense.isdigit():
                    continue
                data[name] = expense
    except OSError:
        print("File cannot be opened", file=sys.stderr)
        sys.exit(2)
    return data


def calculate_budget_variance(dept_info, expense_info):
    """
    Calculates and returns a dictionary containing budget variance information
    for each department. Variance is calculated as: 
    (actual_expenses - budget) / budget * 100
    
    Positive variance means over budget, negative variance means under budget.
    Returns a dictionary where keys are department names and values are 
    variance percentages.
    """
    res = {}
    for name in dept_info.keys():
        actual_expenses = int(expense_info[name])
        budget = int(dept_info[name][0])
        variance = (actual_expenses - budget) / budget * 100
        res[name] = variance
    return res


def determine_over_budget_departments(dept_info, expense_info):
    """
    Determines which departments have exceeded their allocated budget.
    Returns a list of department names that are over budget.
    """
    res = calculate_budget_variance(dept_info, expense_info)
    data = []
    for name in res.keys():
        if res[name] > 0:
            data.append(name)
    return data


def print_over_budget_departments(over_budget_list, dept_info, expense_info):
    """
    Prints the over-budget departments. For each department, print:
    "{} is over budget by ${:,d} ({:.2f}% over)"
    Sort the departments alphabetically.
    
    If no departments are over budget, print "All departments are within budget."
    """
    res = calculate_budget_variance(dept_info, expense_info)
    for name in sorted(over_budget_list):
        actual_expenses = int(expense_info[name])
        budget = int(dept_info[name][0])
        amount_over = actual_expenses - budget
        variance = res[name]
        print(f"{name} is over budget by ${amount_over:,d} ({variance:.2f}% over)")
    if not over_budget_list:
        print("All departments are within budget.")
    

def determine_budget_alerts(dept_info, expense_info):
    """
    Produces a list of strings, where each string represents information
    about a department that requires a budget alert. Budget alerts are required 
    when a department is within +/- 5% of their budget limit (95% to 105% of budget).
    
    Only include departments that require alerts in the result. For each department
    that requires an alert, include a line of the form:
    "{} requires budget monitoring (at {:.2f}% of allocated budget)".
    """
    res = calculate_budget_variance(dept_info, expense_info)
    req_alert = []
    for name in res.keys():
        if -5 <= res[name] <= 5:
            req_alert.append(f"{name} requires budget monitoring (at {100 + res[name]:.2f}% of allocated budget)")
    return req_alert
        

def save_budget_alerts(alert_list):
    """
    Saves each entry of the list to a file named "budget_alerts.txt". The
    entries must be printed in alphabetical order by department name.
    """
    with open("budget_alerts.txt", "w") as file:
        for name in sorted(alert_list):
            file.write(name + "\n")


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
    res = calculate_budget_variance(dept_info, expense_info)
    max_variance = 0
    for variance in res.values():
        max_variance = max(max_variance, abs(variance))
    data = []
    for name, variance in res.items():
        if abs(variance) == max_variance:
            data.append(name)
            if variance > 0:
                under_over = "over"
            else:
                under_over = "under"
    if len(data) >= 2 or max_variance == 0:
        return None
    else:
        return f"{data[0]} had the largest variance at {max_variance:.2f}% ({under_over} budget)"


def calculate_efficiency_metrics(dept_info, expense_info):
    """
    Calculates expense per employee for each department.
    Returns a dictionary where keys are department names and values are 
    expense per employee (actual_expenses / number_of_employees).
    """
    expense_per = {}
    for name in dept_info.keys():
        actual_expenses = int(expense_info[name])
        number_of_employees = int(dept_info[name][1])
        expense_per_employee = actual_expenses / number_of_employees
        expense_per[name] = expense_per_employee
    return expense_per


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
    # 1. Load and process department information
    dept_info = parse_department_information(dept_info_filename)

    # 2. Print department information
    print_department_information(dept_info)

    # 3. Load and process expense information
    expense_info = parse_expense_information(expense_info_filename)

    # 4. Determine and print over-budget departments
    over_budget_list = determine_over_budget_departments(dept_info, expense_info)
    print_over_budget_departments(over_budget_list, dept_info, expense_info)

    # 5. Determine budget alerts and save to file
    alert_list = determine_budget_alerts(dept_info, expense_info)
    save_budget_alerts(alert_list)

    # 6. Determine and print largest variance
    largest_variance = determine_largest_variance(dept_info, expense_info)
    print(largest_variance)

    # 7. Calculate and display efficiency metrics
    efficiency_metrics = calculate_efficiency_metrics(dept_info, expense_info)
    for key, value in sorted(efficiency_metrics.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: ${value:,.2f} per employee")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("files not enough")
        sys.exit(101)

    dept_info_filename = sys.argv[1]
    expense_info_filename = sys.argv[2]

    process(dept_info_filename, expense_info_filename)