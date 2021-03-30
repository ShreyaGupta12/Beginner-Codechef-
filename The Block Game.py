for _ in range(int(input())):
    n=input()
    print('wins' if n[::-1]==n else 'loses')
