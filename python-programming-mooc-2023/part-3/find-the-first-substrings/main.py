string_input = "python"
character_input = "n"

while True:
    index = string_input.find(character_input)
    length = len(string_input[index:index + 3])

    if index >= 0 and length >= 3:
        print(string_input[index:index + 3])
        break
    else:
        break
    