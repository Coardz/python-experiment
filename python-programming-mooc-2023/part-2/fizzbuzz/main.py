# Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

# First let's ask the user for number
number = int(input("Number:"))

# divisible by 5 and 3
if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
# if number divided by 5 == 0 then it's divisible by 5
elif number % 5 == 0:
    print("Buzz")
# if number divided by 3 == 0 then it's divisible by 3
elif number % 3 == 0:
    print("Fizz")