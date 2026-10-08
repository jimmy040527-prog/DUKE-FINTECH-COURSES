# Retirement

For this problem, you will write a "retirement savings" calculator.
We'll remove the effects of inflation by keeping everything in 
"today's dollars" and using a "Rate of return" that is in terms of 
"more than inflation."
 
1. Create a file called `retirement.py`.
2. We will model both savings (while working) and expenditures 
   (while retired).  It turns out that both of these require the same basic 
   information, so we will use a dictionary to track these fields both while
   the individual is working and while the individual is retired.  Each
   dictionary will have three fields:
   - *months*: an int value, the number of months the dictionary applies to
   - *contribution*: a float for how many dollars are contributed 
     (or spent if negative) from the account per month
   - *rate_of_return*: a float for the rate of returns per period (month)
     (which we will assume to be "after inflation").  

   **Note:** Make sure you use these exact key values with lowercase values. 
   The autograder will create its own dictionaries based upon this definition 
   to pass to the retirement function in step 3.

3. Write the function
   ```python 
   def retirement(start_age, initial_savings, working_info, retired_info):
   """
   Prints the current status of an individual's retirement account.
   The dictionaries both have these fields: 
      "months","contribution","rate_of_return"

   Args:
      start_age (int): At what age (in months) does the individual start
      initial_savings (float): initial savings in dollars
      working_info (dict): information about working
      retired_into (dict): information about retirement

   Returns:
   None
   """
   ```
   This function performs two similar tasks (look for a chance to abstract 
   something out into a function!).
    
   First, it should compute your retirement account balance each month while you are working.  To do this, you need to calculate the account balance
   increase from returns (balance * rate of return), and add that to the
   current balance.  You then need to add the monthly contribution to the
   balance.

   For example, if you have $1,000 in the account, earn a 0.5% rate of return per month, and contribute $100 per month, you would compute 1000 * 0.005 = $5 in interest earned.  You would then add this plus the monthly contribution to the balance to end up with $1105 in the account at the end of the month.

   At the start of each month (before the balance changes), you should print out the current balance with the following format:
   ```
   "Age {:3d} month {:2d} you have ${:,.2f}"
   ```
   
   The first two format conversions are the savers age in years and months.
   The third format conversion is the account balance
   This calculation goes on for the number of months specified  in the "working" retire_info structure. 

   Second, you should perform a very similar calculation for each month of
   retirement.  The difference here is that you will use the information in the
   "retired" retire_info structure instead of the information in the "working" 
   structure.  As with working, you should print out the same information as before.

   Hint: since you are performing a very similar computation, think about how you can abstract that computation out into a function, and re-use it, rather than re-writing it.

4. After the function, write code the computes the retirement, assuming
   ```text
     Working:
     --------
      Months: 489
      Per Month Savings: $1000
      Rate of Return:  4.5% per year ( 0.045/12 per month) 
                       [above inflation]
    Retired:
    --------
      Months: 384
      Per Month Spending: -4000
      Rate of Return: 1% per year ( 0.01/12 per month) 
                      [above inflation]
    Starting conditions:
    -------------------
       Age: 327 months (27 years, 3 months)
       Savings: $21,345
   ```

   You will need to create your dictionary objects and then call retirement()

5. Run your code and compare your output against `retirement_ans.txt`.

   From the command line, you can compare two files with the command `diff`.

   To compare two files, execute `diff file1 file2`

   You can see more information on the `diff` command with `man diff`.
      
6. Submit `retirement.py`
