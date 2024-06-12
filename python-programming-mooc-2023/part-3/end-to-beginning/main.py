# so the last in array is -1 -2 -3 -4
# also we can use len(string) imagine if word it's len = 4 - 1 we get 3 and the 3 is = d

string = "abc"
string = input("Please type in a string: ")
index = len(string)
while index != 0:
    index -= 1
    print(string[index])