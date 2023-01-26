#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    expanded = []
    n = len(values)
    for i in range(n):
        for j in range(freqs[i]):
            expanded.append(values[i])
    expanded = sorted(expanded)
    n = len(expanded)
    mid = n//2
    mid2 = mid//2
    if n%2==0:
        q1 = (expanded[mid2-1] + expanded[mid2])/2
        q3 = (expanded[mid+mid2-1] + expanded[mid+mid2] )/2
    else:
        q1 = expanded[mid2]
        q3 = expanded[mid+mid2]
    print("{:.1f}".format(q3-q1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
