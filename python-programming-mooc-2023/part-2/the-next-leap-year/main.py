# Write your solution here


year = int(input("Year:"))
next = year

while True:
    next =+ 1
    
    if next % 4 == 0:
        break


print(f"The next leap year after {year} is {next}")