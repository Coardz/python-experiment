while True:
    
    number = int(input("Please type in a number:")) # This 3
    lower = 1
    
    if number <= 0:
        print("Thanks and Bye!")
        break
    else:
        for i in range(1,number + 1):
            lower = lower*i
        print(lower)
        continue