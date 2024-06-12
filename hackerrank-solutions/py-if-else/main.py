#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    # check if odd
    if n % 2 != 0:
        print("Weird")
    # check if it's in 2 to 5 and if it's even
    elif n >= 2 and n <= 5 and n % 2 == 0:
        print("Not Weird") 
    # check if it's in 6 to 20 and if it's even
    elif n >= 6 and n <= 20 and n % 2 == 0:
        print("Weird")
    # check if it's more than 20 and if it's even
    elif n > 20 and n % 2 == 0:
        print("Not Weird")