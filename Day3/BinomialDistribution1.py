def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

boys, girls = map(float,input().split())
total = boys + girls
p = boys/total
q = girls/total
total = 0
for i in range(3,7):
    total += nCr(6,i) * ((p**i)*(q**(6-i)))
print(round(total,3))
