
try:
    n = int("a")
except ValueError:
    print("ValueError: Unable to cast letter into an integer.")
else:
    print(n)
finally:
    print("Let's try another one.")
 
print()
    
try:
    j = srt(8)
except NameError:
    print("NameError: Invalid function name call.")
else:
    print(j)
finally:
    print("Let's try another one.")
    
print()
    
try:
    s = "James has " + 3 + " cars"
except TypeError:
    print("TypeError: Invalid concatenation expression.")
else:
    print(s)
finally:
    print("Let's try another one.")
    
# try-except statements do not catch syntax errors.