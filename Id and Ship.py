code={'b':'BattleShip','c':'Cruiser','d':'Destroyer','f':'Frigate'}
for _ in range(int(input())):
    print(code[(input().strip()).lower()])
