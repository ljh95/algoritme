n, m = map(int, input().split())
x, y, d = map(int, input().split())

steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
maps =[]
for i in range(n):
    maps.append(list(map(int, input().split())))

count = 1
while True:
    isMove = False
    for i in range(4):
        idx = (d+i+1) % 4
        n_x = x + steps[idx][0]
        n_y = y + steps[idx][1]
        if maps[n_y][n_x] == 0:
            d = idx
            x, y = n_x, n_y
            maps[y][x] = 2
            count+=1
            isMove = True
            break
    if isMove == False:
        n_x = x - steps[d][0]
        n_y = y - steps[d][1]
        if maps[n_y][n_x] == 2:
            x, y = n_x, n_y
        else:
            break

print(count)
