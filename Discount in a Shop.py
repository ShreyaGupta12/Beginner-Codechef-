for _ in range(int(input())):
    s=input()
    ans=1e15
    for i in range(len(s)):
        if(i==0): s1=s[1:]
        elif(i==len(s)-1): s1=s[:-1]
        else: s1=s[:i]+s[i+1:]
        ans=min(ans,int(s1))
    print(ans)
