# HackerRank - Super Digit
#
# Question:
# Given a number n and an integer k, repeat n k times and find
# the super digit by repeatedly adding its digits until a
# single digit remains.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    
    
    x=sum(int(digit) for digit in n)*k
    while x>=10:
        sum1=0
    
        while x>0:     
            digit=x%10
            sum1+=digit
            x=x//10
        x=sum1
            
    return x
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
