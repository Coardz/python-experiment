def chessboard(n):
    char1=""
    char2=""
    for i in range(n):
        if i % 2 == 0:
            char1 += "1"
            char2 += "0"
        else:
            char1 += "0"
            char2 += "1"
            
    for i in range(n):
        if i % 2 == 0:
            print(char1)
        else:
            print(char2)
chessboard(3)

""""
Notes

i = 0

so 0 % 2 == 0 because it's already zero bro
then it add

char1="1"
char2="0"

second loop i = 1

so we know that i % 2 == 0 is false
so it adds

char1="10"
char2="01"

third loop is i = 2 which is even

char1="101"
char2="010"

for printing

we still loop with if statement

so on first i is equivalent to 0

it will output char1 which is 101

on second i it's equivalent to 1 which is false

it will output char2 which is 010

i = 2
on third it's even os it will output char1 which is 101
"""

""""
Output
101
010
101
"""