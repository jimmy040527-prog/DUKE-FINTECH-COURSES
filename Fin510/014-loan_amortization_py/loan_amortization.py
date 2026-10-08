def calculate_monthly_payment(loan_amount, months, monthly_rate):
    """
    Calculate the monthly payment for a loan.
    """
    if monthly_rate == 0:
        monthly_payment = loan_amount / months
    else:
        monthly_payment = ((loan_amount * monthly_rate * (1 + monthly_rate) ** months) /
                           ((1 + monthly_rate) ** months - 1))
    return monthly_payment


def calculate_loan_amortization(loan_amount, loan_terms, interest_rates):
    """
    Calculate and display a loan amortization table for different loan terms and interest rates.

    Algorithm:
    1. Initialize a variable to store total interest paid across all screnarios
    2. Print header with loan amount
    3. Print table header with Years label followed by interest rates
    3. For each loan term:
       a. Print the term cell.   Use 5 spaces for the term
       b. For each interest rate:
          i. Calculate monthly payment using the formula:
             Monthly payment = (P * r * (1+r)^n) / ((1+r)^n - 1) where:
             - P is the loan amount
             - r is the monthly interest rate (annual rate / 12 / 100)
             - n is the total number of months (term * 12)
          ii. Total amount paid = monthly payment * number of months
          iii. interest paid = total amount paid - loan amount
          iv. Add interest paid to the total interest paid
          v. print the monthly payment in a cell of 9 spaces, with $ next to the payment
    4. Return total interest paid across all scenarios
    """
    # Implement your code here
    total_interest = 0
    print(f'Loan Amount: ${loan_amount:,.2f}')
    print()

    # table header
    print('Years', end="")
    for rate in interest_rates:
        print(f"{rate:8.2f}%", end="")
    print()

    for term in loan_terms:
        print(f"{term:5}", end="")
        num_month = term * 12

        for annual_rate in interest_rates:
            monthly_rate = annual_rate / 12 / 100
            Monthly_payment = calculate_monthly_payment(loan_amount, num_month, monthly_rate)
            total_paid = Monthly_payment * num_month
            interest_paid = total_paid - loan_amount
            total_interest += interest_paid
            payment = f"${Monthly_payment:,.2f}"
            cell = f"{payment:>9}"
            print(cell, end="")
        print()
    return total_interest


# Loan of $10,000 with terms of 1, 3, 5, 10, 15, and 30 years
# and interest rates from 2% to 10%
loan_terms = [1, 3, 5, 10, 15, 30]
interest_rates = [2, 3, 4, 5, 6, 7, 8, 9, 10]

total_interest = calculate_loan_amortization(10000, loan_terms, interest_rates)
print(f"\nTotal interest across all scenarios: ${total_interest:,.2f}")
