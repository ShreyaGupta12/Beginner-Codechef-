for _ in range(int(input())):
    n, k = map(int, input().split())
    l = input().split()
    m = []
    for i in range(k):
        m += input().split()
    for i in range(n):
        print("YES" if l[i] in m else "NO")
