n,m,k=map(int,input().split())
c=0
for i in range(n):
    arr=list(map(int,input().split()))
    if arr[-1]<=10 and sum(arr)-arr[-1]>=m:
        c+=1
print(c)
