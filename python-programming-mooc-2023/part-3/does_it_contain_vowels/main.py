string = input("Please type in a string: ")
vowels = "aeo" # this the vowels that we must find | 0 = a | 1 = e | 2 = o | 
index = 0 # starting point
 
while index < len(vowels): # if 0 < 3
    vowel = vowels[index] # catch the vowels for example test a is not in | e is in it will execute the if statement
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1 # increment