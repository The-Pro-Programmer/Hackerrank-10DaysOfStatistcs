#!/bin/python3

import os
import statistics as st


#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    op = []
    n = len(arr)
    arr.sort()
    op.append(int(st.median(arr[0:n // 2])))
    if (n % 2 == 0):
        op.append(int(st.median(arr)))
        op.append(int(st.median(arr[n // 2:n])))
    else:
        op.append(int(arr[n // 2]))
        op.append(int(st.median(arr[1 + (n // 2):n])))
    return op


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
