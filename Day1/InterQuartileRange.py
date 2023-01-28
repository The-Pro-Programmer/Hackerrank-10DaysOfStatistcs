#!/bin/python3

import statistics as st


#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    iqr = 0
    n = len(values)
    data = []
    for i in range(n):
        data += [values[i]] * freqs[i]
    data.sort()
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        q3 = st.median(data[mid:])
    else:
        q3 = st.median(data[mid + 1:])
    q1 = st.median(data[:mid])
    print(round(float(q3 - q1), 1))


if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)
