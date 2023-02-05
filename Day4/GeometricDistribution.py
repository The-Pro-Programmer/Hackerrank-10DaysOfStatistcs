# Enter your code here. Read input from STDIN. Print output to STDOUT
def geometric_distributon(n, p):
    return ((1-p)**(n-1))*p

numerator, denominator = list(map(int, input().split()))
n = int(input())
probability = numerator/denominator
print('{:.3f}'.format(geometric_distributon(n, probability)))
