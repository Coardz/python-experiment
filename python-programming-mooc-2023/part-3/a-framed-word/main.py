word = input("Word: ")
row = "*"
times = 30

start = (28 - len(word)) // 2

if len(word) % 2 == 0:
    end = start 
else:
    end = start + 1

print(row * times)
print("*" + " " * start + word + " " * end + "*")
print(row * times)