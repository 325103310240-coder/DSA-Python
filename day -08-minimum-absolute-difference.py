#minimum absolute difference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    result=[]
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            result.append(abs(arr[i]-arr[j]))
    x=result[0]
    for i in range(1,len(result)):
        if result[i]<x:
            x=result[i]
    return x
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
