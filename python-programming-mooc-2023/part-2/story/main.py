# Write your solution here
sentence = [""]

while True:
    word = str(input("Please type in a word:"))
    if word != "end" and word != sentence[-1]:
        sentence.append(word)
    else:
        break

sentence = ' '.join(sentence[1:])
print(sentence)