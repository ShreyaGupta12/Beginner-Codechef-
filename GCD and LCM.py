def gcd(a,b):
    if b==0: return a
    else: return gcd(b,a%b)
for _ in range(int(input())):
    a,b=map(int,input().split())
    h=gcd(a,b)
    print(h,((a*b)//h))
