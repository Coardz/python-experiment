number = [1, 2, 3, 4]   * 2 # the index start with 0 so it means the number 1 is equal to 0

print(number) #output [1,2,3,4, 1, 2, 3, 4]

number = [1, 2, 3, 4]

A = [number] * 2
print(A) # output [[1, 2, 3, 4], [1, 2, 3, 4]]


# Explanation
# this excutes first A = [number] * 2 which output [[1, 2, 3, 4], [1, 2, 3, 4]]
# then number[2]=45 which output [[1, 2, 45, 4], [1, 2, 45, 4]]

number[2] = 7 # changed the value of 2 to 45
print(A) # output [[1, 2, 45, 4], [1, 2, 45, 4]]

names = ["ben", "boo", "sir", "zed", "bob"] # the index start with 0 so it means the number 1 is equal to 0

if "sir" in names: # if "sir" is on array it will follow the statement below will be executed
    print("Success")
    print(f"Theres {len(names)} names in Array") #output [1,2,3,4, 1, 2, 3, 4]
else: # if the array doesn't contain "sir" the statement below will be executed
    print("Failed")


