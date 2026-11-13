name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

name_1 = name_1.lower()
name_2 = name_2.lower()
name_3 = name_3.lower()

print(name_1)
print(name_2)
print(name_3)

name_1 = name_1.title()
name_2 = name_2.title()
name_3 = name_3.title()

print(name_1)
print(name_2)
print(name_3)

salary_1 = salary_1.replace("$", "")
salary_2 = salary_2.replace("$", "")

print(salary_1)
print(salary_2)

print(type(salary_1))
print(type(salary_2))

#In order to perform math on the salaries, you need to remove the commas and cast them into integers.

salary_1 = int(salary_1.replace(",", ""))
salary_2 = int(salary_2.replace(",", ""))

print(salary_1)
print(salary_2)

print(type(salary_1))
print(type(salary_2))