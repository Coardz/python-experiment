# Write your solution her
def spruce(times):
    i = times
    leaves = "*"
    print("a spruce!")
    while times > 0:
        times -= 1
        print(" " * times + leaves)
        leaves += "**"
    print(" " * (i-1) + "*") # fucking dirty ass code hahaha so fuckig messy
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)