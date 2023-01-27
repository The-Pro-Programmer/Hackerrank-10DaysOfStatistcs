#!/bin/python3

import statistics as st
import math

def stdDev(arr):
    mean = st.mean(arr)
    n = len(arr)
    meanDifference = 0
    for i in range(n):
        meanDifference += math.pow(mean-arr[i], 2)
    print(round(math.sqrt(meanDifference/n), 1))

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    stdDev(vals)
