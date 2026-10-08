# Loan Amortization Table

Open the provided `loan_amortization.py` file. You will see one function 
`calculate_loan_amortization`, along with some code that will call that function.

The `calculate_loan_amortization` function has an algorithm written as comments, 
but no code. Translate this algorithm to code.

## Assignment Description
In this assignment, you will implement a function that creates loan amortization 
tables for different loan terms and interest rates. The tables will show monthly 
payments, total amount paid, and total interest paid for a loan.

The `calculate_loan_amortization` function should:
1. Take parameters for loan amount, a list of loan terms in years, and a list of 
   annual interest rates
2. Create an amortization table with the monthly payment amounts for each 
   combination of term and interest rate
3. Return the total interest that would be paid across all scenarios combined

After implementing the function, execute your code with `python3 loan_calculator.py`.

If your program has any errors, the interpreter will do its best to describe 
what is wrong. If a problem exists, look at the code and try to see where you 
did not follow the syntax rules from the different notebooks. The line number 
and message it gives may help you find the problem. If you cannot find the 
problem after a few minutes, ask for help.

If your code has legal syntax, your program should run and produce output. 
Compare this output with the output we expect.

If they are the same, submit your assignment for grading.

If they are not, try to fix the problem (and ask for help if you cannot).

## Expected output

```text
Loan Amount: $10,000.00

Years     2.00%    3.00%    4.00%    5.00%    6.00%    7.00%    8.00%    9.00%   10.00%
    1   $842.39  $846.94  $851.50  $856.07  $860.66  $865.27  $869.88  $874.51  $879.16
    3   $286.43  $290.81  $295.24  $299.71  $304.22  $308.77  $313.36  $318.00  $322.67
    5   $175.28  $179.69  $184.17  $188.71  $193.33  $198.01  $202.76  $207.58  $212.47
   10    $92.01   $96.56  $101.25  $106.07  $111.02  $116.11  $121.33  $126.68  $132.15
   15    $64.35   $69.06   $73.97   $79.08   $84.39   $89.88   $95.57  $101.43  $107.46
   30    $36.96   $42.16   $47.74   $53.68   $59.96   $66.53   $73.38   $80.46   $87.76

Total interest across all scenarios: $211,706.23
```

## Note:
To print the $ next to the payment amount and maintain the appropriate amount
of spaces/paddding you'll need to do this in two formatting steps
```python
monthly_payment = 869.88
payment = "${:,.2f}".format(monthly_payment) # format number to 2 decimal places
cell    = "{:>9}".format(payment)            # right-align payment string
```
