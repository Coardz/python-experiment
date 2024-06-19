number = int(input("Please Enter a Number"))
limit = 10
if number > limit:
    print(number, "Is More Than", limit)
else:
    while number < 10:
        number += 1
        if number == 5:
            print("You Reach 5")
            continue
    
print(number)