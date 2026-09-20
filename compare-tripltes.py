import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def compareTriplets(a, b):
    c=0
    d=0
    for i in range(len(a)):
        if a[i]>b[i]:
            c=c+1
            d=d+0
    
        elif a[i]<b[i]:
            d=d+1
            c=c+0
            
        else:
            d=d+0
            c=c+0
    return c,d
            
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
