working_hour = float(input("How many hours did the employee work? "))
pay_rate = float(input('What is the employees pay rate? '))
if working_hour <= 40:
    Total_pay = working_hour * pay_rate
else:
    overtime_hours = working_hour - 40
    Total_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
print(f'Total pay: {Total_pay:.4f}')
tax_rate = 0.2
Taxes = tax_rate * Total_pay
print(f'Taxes: {Taxes:.4f}')
Net_pay = Total_pay - Taxes
print(f"Net pay: {Net_pay:.2f}")


