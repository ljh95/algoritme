n = int(input())
plans = input().split()
x, y = 1, 1
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
arrows = ['L', 'R', 'U', 'D']
for plan in plans:
    for i in range(len(arrows)):
        if arrows[i] == plan:
            nx, ny = x + moves[i][0], y + moves[i][1]

            if nx < 1 or nx > n-1 or ny < 1 or ny > n-1:
                continue
            x, y = nx, ny
print(x, y)