from collections import deque
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

queue = deque()
queue.append((0, 0))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

arr[0][0] =2

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            continue
        if arr[nx][ny] == 1:
            queue.append((nx, ny))
            arr[nx][ny] = arr[x][y] + 1
print(arr[n-1][m-1]-1)