# net worth = total assets - total liabilities

# Assets
liquid_assets = 327439
investments = 85217
real_estate = 964532
personal_property = 61058
total_assets = liquid_assets + investments + real_estate + personal_property

#Liabilities
mortgage = 12465
vehicle_loans = 3460
student_loans = 0
credit_loans = 1375
total_debt = mortgage + vehicle_loans + student_loans + credit_loans

net_worth = total_assets - total_debt

print(f"Your total assets are {total_assets}")
print(f"Your total debts are {total_debt}")
print(f"Your net worth is {net_worth}")