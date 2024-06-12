n = int(input()) # how many guest we have
names = [] # this is the container of names

for _ in range(n): # loops to ask for names
    name = input("") # asking guest name
    names.append(name) # adding all the name into names

for name in names: # loops to print out 
    print(f"Takk {name}")