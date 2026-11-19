def displaying_mailing_label(name,address,city,state,zip):
    print(f"{name}\n{address}\n{city}, {state} {zip}")
    
def add_numbers(*numbers):
    total = ""
    for number in numbers:
        total += f"{str(number)} + "
    
    print(f"{total[:len(total) - 3]} = {sum(numbers)}")
    
def display_receipt(total_due,amount_paid):
    
    print(f"Total Due: ${total_due:,.2f}")
    print(f"Amount Paid: ${amount_paid:,.2f}")
    print()
    
    if amount_paid < total_due:
        print(f"Remaining Balance: ${total_due - amount_paid}")
    else:
        print(f"Change Due: ${amount_paid - total_due:,.2f}")
        
        
displaying_mailing_label("John Doe", "110 Maxwell Ct.", "Philadelphia", "PA", "40657")
print()
displaying_mailing_label("Bertrand Harrison", "2339 Bolzano St.", "New Orleans", "LA", "15300")
print()
add_numbers(5)
print()
add_numbers(11,7)
print()
add_numbers(29,57,49,13)
print()
display_receipt(14.50,15)
print()
print()
display_receipt(7.45,7.45)
print()
print()
display_receipt(24.75,22.75)

