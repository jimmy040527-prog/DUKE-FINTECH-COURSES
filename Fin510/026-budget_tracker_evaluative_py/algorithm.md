# Budget Tracker

## Determine Largest Variance

1. initialize a max_variance as 0 

2. using calculate_budget_variance() get all variance and then go through all variance by using for loop to find the max_variance (also use abs() which is a built_in func)

3. initialize a blank list

4. go through all the variance and find which department got the largest absolute variance and add to the list, also decide whether it is under or over budget.

5. if list has more than 1 name or max_variance == 0: return None

6. return the correct answer

## Tests

- Case A: The department which has the largest variance is over_budget 
IT: +12.5%
Marketing: +5%
HR: - 6%

- Case B: The department which has the largest variance is under_budget
IT: -12.5%
Marketing: +5%
HR: +6%

- Case C: There's tie in largest variance
IT: -12.5%
Marketing: +12.5%
HR: +6%

- Case D: All variance == 0
IT: 0%
Marketing: 0%
HR: 0%

