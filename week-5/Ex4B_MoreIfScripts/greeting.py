hour = 5

if hour >= 23 or hour <= 4:
    print("What are you doing up so late?")
elif hour >= 17 and hour < 23:
    print("Good evening!")
elif hour >= 10:
    print("Good day!")
elif hour > 4:
    print("Good morning!")
