dept_code = 10

match dept_code:   
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
        
# The match case is the most efficient solution. It is also the easiest to read and understand.