string = input("Please tpye in a string:")
length = len(string) - 1
limit = 0
while length >= limit:
    print(string[length:])
    length -= 1