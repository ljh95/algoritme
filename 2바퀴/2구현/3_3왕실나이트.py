string = input()
x = int(string[1])
y = ord(string[0]) - ord('a') + 1

print('row, column =', x, y)

moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
count = 0
for move in moves:
    nx, ny = x + move[0], y + move[1]

    if nx < 1 or nx > 7 or ny < 1 or ny > 7:
        continue
    count += 1
print(count)