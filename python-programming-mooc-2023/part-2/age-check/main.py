# Write your solution here
age = int(input("What is your age?"))

if age > 0 and age < 5:
    print("I suspect you can't write quite yet...")
elif age > 5:
    print(f"Ok you're {age} years old")
else:
    print("That must be a mistake")
