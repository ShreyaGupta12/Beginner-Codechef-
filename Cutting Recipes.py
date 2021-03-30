from math import gcd
for _ in range(int(input())):
    l=list(map(int,input().split()))
    a=l[1]
    for i in l[1:]: a=gcd(a,i)
    for i in l[1:]: print(i//a)
