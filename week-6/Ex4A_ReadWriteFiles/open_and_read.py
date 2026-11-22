with open("about_me.txt", "r") as f:
    #print(f.read(50))
    #print(f.read(50))
    #In the output, the code broke up the text. From what I can observe the .read(50) reads the first 50 characters of the text.
    
    #print(f.readline(50))
    #print(f.readline())
    
    #for i in range(1, 5):
    #    print(f.readline())
    
    #print(f.readlines(1))
    # .readlines(1) returns an array containing the first line of text.
    
    #print(f.readlines(1))
    # # the second .readlines(1) returns an array containing the second line.
    
    #print(f.readlines(10))
    # .readlines(10) returns an array containing the third line of text.
    
    #print(f.readlines(10))
     # the first .readlines(10) returns an array containing the first of text, and the second one contains the second line.
     
    #print(f.readlines(100))
    # .readlines(100) returns an array containing three lines of text.
    
    #print(f.readlines(-1))
    # .readlines(-1) returns an array containing all lines of text.
    
    first_fifty = f.read(50)
    
    next_four = []
    
    for i in range(1,5):
        next_four.append(f.readline())
        
    next_hundred = f.readlines(100)
    
    print(f"First 50 characters: {first_fifty}")
    print(f"Next four lines, as list by line: {next_four}")
    print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_hundred}")
    
    