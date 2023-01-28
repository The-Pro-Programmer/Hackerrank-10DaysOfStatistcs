# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import statistics as st

n = int(input())
data = list(map(int, input().split()))

data.sort()
mean = round(sum(data)/n, 1)
if n%2==0:
    median = round((data[(n//2)-1] + data[n//2])/2, 1)
else:
    median = data[n//2]
mode = round(st.mode(data), 1)

print(mean)
print(median)
print(mode)
