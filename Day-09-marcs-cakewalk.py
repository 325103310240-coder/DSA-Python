# HackerRank - Marc's Cakewalk
#
# Question:
# Given the calorie counts of cupcakes, determine the minimum
# number of miles Marc must walk to maintain his weight.
# He can eat the cupcakes in any order.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    add=0
    calorie.sort(reverse=True)
    j=0
    for i in range(len(calorie)):
        
        
        add=add+((2**j)*calorie[i])
        j+=1
        
    return add
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
