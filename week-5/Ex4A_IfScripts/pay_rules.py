pay_rate = 17.30
hours_worked = 45
gross_pay = 0
reason = ""

if hours_worked > 40:
    gross_pay = (pay_rate * 40) + ((1.5*pay_rate) * (hours_worked - 40))
    reason = "Over 40 hours"
elif hours_worked == 40:
    gross_pay = pay_rate * hours_worked
    reason = "Exactly 40 hours"
else:
    gross_pay = pay_rate * hours_worked
    reason = "Under 40 hours"

print(f"{pay_rate}   {hours_worked}   {gross_pay}   {reason}")
    