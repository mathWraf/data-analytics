student_name = "Lucas"
student_major = "ENGR"

match student_major:
    case "BIOL":
        print("Major: Biology")
        print("Department Office: Science Bldg, Room 310")
    case "CSCi":
        print("Major: Computer Science")
        print("Department Office: Sheppard Hall, Room 314")
    case "ENG":
        print("Major: English")
        print("Department Office: Kerr Hall, Room 201")
    case "HIST":
        print("Major: History")
        print("Department Office: Kerr Hall, Room 114")
    case "MKT":
        print("Major: Marketing")
        print("Department Office: Westly Hall, Room 310")
    case _:
        print("Major: <unknown>")
        print("Department Office: <unknown>")