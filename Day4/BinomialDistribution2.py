def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

rejected, batchSize = map(float,input().split())
rejected /= 100
notRejected = 1 - rejected

total1 = 0
for i in range(0,3):
    total1 += nCr(batchSize,i) * ((rejected**i)*(notRejected**(batchSize-i)))
print(round(total1, 3))

total2 = 0
for i in range(2, int(batchSize)):
    total2 += nCr(batchSize,i) * ((rejected**i)*(notRejected**(batchSize-i)))
print(round(total2, 3))
