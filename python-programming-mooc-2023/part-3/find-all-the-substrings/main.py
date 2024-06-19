input_string = "mammoboth"
input_character = "m"

while True:
    index = input_string.find(input_character)
    input_string = input_string[index:]
    length = len(input_string[index:index+3])
    
    if index >= 0 and length >= 3:
        print(input_string[index:index+3])

    if len(input_string) == 0:
        print("Empty")
        break
    


    input_string = input_string[2:]