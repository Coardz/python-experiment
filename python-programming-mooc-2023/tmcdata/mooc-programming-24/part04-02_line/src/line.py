# Write your solution here

def line(times, word):
    if word == "":
        print("*" * times)
    else:
        print(word[0] * times)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(5, "")
    line(4, "dawg")