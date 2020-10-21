n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

worked = [[0]*m for _ in range(n)]
worked[x][y] = 2

d_count = 0
count = 1
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def turn_left():
    global d
    d =  (d+3)%4

def turn_back():
    global d
    d =  (d+2)%4

while True:
    for i in range(4):
        turn_left()
        nx, ny = x + moves[d][1], y + moves[d][0]
        # 벽을 넘어서거나, 앞이 1이거나 이미 가봤던 곳이거나.
        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
            d_count+=1
            continue
        if arr[nx][ny] == 1 or worked[nx][ny] == 2:
            d_count+=1
            continue
        worked[x][y] = 2
        x, y = nx, ny
        count+=1
        d_count = 0
        break
    if d_count == 4: # 4 방향 모두 가봤던 곳이거나 바다이다
        back = 4%(d+2)
        nx, ny = x+moves[back][0], y+moves[back][1]
        if nx<0 or nx>m or ny<0 or ny>n or arr[nx][ny] == 1:
            break
        elif worked[nx][ny] == 2:
            d = back
            d_count = 0
        else:
            print("err! print back, nx, ny = ", back, nx, ny)

print(count)