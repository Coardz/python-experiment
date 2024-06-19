# Copy here code of line function from previous exercise and use it in your solution
def line(width, word):
    if word == "":
        print(width * "*")
    else:
        print(width * word[0]) # imagine the character / if with 5 it will look liek this /////
        
def shape(width, word, height, filler,):
    
    i = 1
    while i <= width:
        line(i, word)
        i += 1
    
    x = 0
    while x < height:
        line(width, filler)
        x += 1
        # while i <= width:
        #     line(i, word)
        #     i += 1
    
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(2, "o", 4, "+")