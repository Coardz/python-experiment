# Write your solution here

input_string = "methodology"
input_substrings = "o"
times = 0

while True:
    index = input_string.find(input_substrings) # find where array it starts
    
    if index >= 0:
        times += 1

    if times == 2:
        double = True
        break
    
    if len(input_string) < 0:
        break
    
    input_string = input_string[index+1:]

if double == True:
    print(f"The Second occurence of the substring is at index {index}")
else:
    print("The substring does not occur twice in the string.")