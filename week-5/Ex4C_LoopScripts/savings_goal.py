bank_balance = 25000
savings_goal = 67000
weekly_savings = 3700
treat = 250
half_milestone = False
second_quarter_milestone = False

while bank_balance < savings_goal:
    bank_balance += weekly_savings
    
    if bank_balance >= 0.5 * savings_goal and half_milestone is False:
        half_milestone = True
        print(f"Almost there! This week my balance is up to {bank_balance}.")
    elif bank_balance >= 0.75 * savings_goal and second_quarter_milestone is False:
        second_quarter_milestone = True
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to {bank_balance}.")
    else:
        print(f"This week my balance increased to {bank_balance}")
        
print(f"Goal met! My current balance is {bank_balance}.")