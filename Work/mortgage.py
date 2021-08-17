# mortgage.py
'''Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.'''
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

# Extra payments ...
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month_count = 0
special_payment = payment + extra_payment

while principal > 0:
    month_count += 1
    principal = principal * (1 + rate/12)

    if (month_count >= extra_payment_start_month) and (month_count <= extra_payment_end_month):
        monthly_payment = special_payment
    else:
        monthly_payment = payment    
    
    if monthly_payment > principal:
        monthly_payment = principal  # don't overpay...

    principal = principal - monthly_payment
    total_paid = total_paid + monthly_payment
    print(month_count, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Number of Months', month_count)
