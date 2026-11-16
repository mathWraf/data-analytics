sales_data = [
('Marcus Webb', 'East', 4250.00),
('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
('LaTonya Rivers', 'South', 6420.00),
('Bob Nguyen', 'West', 4980.25),
]

for sale in sales_data:
    print(f"{sale[0]}({sale[1]}): ${sale[2]:,.2f}")
    
    if sale[2] > 5000:
        print(" ^ Top performer!")