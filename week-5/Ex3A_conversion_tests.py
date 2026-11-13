# Description: This script tests various numeric
# conversion techniques
# Author: Matthew Pena

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '


print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))



'''
5a) Casting int()

    Casting variables a, c, and d produced a valuer error. Only variable b was able to be casted.
    
5b) Casting float()

    Casting variables a, c, and d produced a valuer error. Only variable b was able to be casted.
    
5c) Using int(float(a))
    Casting variable a into a float and then integer threw a value error because variable a contained whitespaces.
 '''   
    
#5d) 

new_a = float(a[1:6])
new_b = int(b)
new_c = int(c[:3])
new_d = int(d[7])

print(new_a)
print(new_b)
print(new_c)
print(new_d)

#5e)

print(a.strip(" "))
print(d.strip(" "))


