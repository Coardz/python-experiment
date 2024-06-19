# Write your solution here

input_sentence = "Humpty Dumpty sat on a wall"
#We use split

list = input_sentence.split() # ['Humpty', 'Dumpty', 'sat', 'on', 'a', 'wall']

for word in list:
    print(word[0])