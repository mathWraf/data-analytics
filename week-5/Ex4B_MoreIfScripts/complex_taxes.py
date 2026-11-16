pay_rate = 17.30
hours_worked = 45
gross_pay = 0
annual_pay = pay_rate * hours_worked * 48
file_status = "joint"
tax_rate = 0
weekly_tax = 0
reason = ""

if file_status == "joint":
    if annual_pay >= 75000:
        tax_rate = 0.2
    elif annual_pay >= 25000:
        tax_rate = 0.11
    elif annual_pay >= 12000:
        tax_rate = 0.06
    else:
        tax_rate = 0
else:
    if annual_pay >= 75000:
        tax_rate = 0.2
    elif annual_pay >= 25000:
        tax_rate = 0.15
    elif annual_pay >= 12000:
        tax_rate = 0.1
    else:
        tax_rate = 0.05

if hours_worked > 40:
    gross_pay = (pay_rate * 40) + ((1.5*pay_rate) * (hours_worked - 40))
    reason = "Over 40 hours"
elif hours_worked == 40:
    gross_pay = pay_rate * hours_worked
    reason = "Exactly 40 hours"
else:
    gross_pay = pay_rate * hours_worked
    reason = "Under 40 hours"
    
weekly_tax = tax_rate * gross_pay

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is {gross_pay}")
print(f"Your filing status is {file_status}")
print(f"Your tax withholding for the week is ${weekly_tax}")
print(f"Your net pay is ${gross_pay - weekly_tax}")