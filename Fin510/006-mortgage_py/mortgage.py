p = input("What is the amount borrowed?")
r = input("What is the annual interest rate - express this as a decimal such as 0.07 for 7%?")

# place your code here after this line
n = 30 * 12
a = float(p) * (float(r) / 12) * (1 + float(r) / 12) ** (n) / ((1 + float(r) / 12) ** n - 1)
payment_amount = int(a * 100) / 100
print(payment_amount)
