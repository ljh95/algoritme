from collections import deque

def move_d(d, C):
    if C == 'L':
        return (d+5)%4
    else:
        return (d+3)%4

def delete_tail(isDelete, snake):
    if isDelete:
        snake.popleft()


snake = deque() # 뱀의 위치 index
apples = []
moves = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
maps = [[0] * N for _ in range(N)]

a = int(input())
for i in range(a): # 사과의 위치를 2로 바꿈
    x, y = map(int, input().split())
    maps[x-1][y-1] = 2

b = int(input())
for i in range(b):
    x, y = input().split()
    moves.append((int(x), y))



snake.append((0, 0)) # 뱀의 첫 위치
maps[0][0] = 1
d = 3 # 처음 바라보는 방향 = 오른쪽
count = 0
isDone = False
isDelete = True
last_X = 0
for i in range(len(moves)):
    X, C = moves[i]
    X -= last_X
    print("X: ", X)
    for j in range(X):
        print("snake: ", snake)
        count+=1
        # print("snake: ", snake)
        head = snake.pop()
        snake.append(head)
        # print("head: ", head)
        nx = head[0] + dx[d]
        ny = head[1] + dy[d]
        # 벽에 부딪치는지?
        if nx < 0 or ny < 0 or nx >= N or ny >= N: 
            print("벽에 부딪침")
            print(count)
            isDone = True
            break
        # 자기 몸에 부딪치는지?
        if (nx, ny) in snake:
            print("자기 몸에 부딪침")
            print(count)
            isDone = True
            break
        # 사과를 만났는지?
        if maps[nx][ny] == 2:
            # print("사과 먹음")
            maps[nx][ny] = 0
            isDelete = False
        # 일단 안전한 위치이니 다음 위치를 넣고 마지막 위치를 뺀다.
        snake.append((nx, ny))
        if isDelete:
            # print("꼬리를 삭제합니다.")
            snake.popleft()
        isDelete = True
    
    if isDone:
        break
    # 한 방향으로 다 이동하면 방향을 결정한다.
    last_X += X
    d = move_d(d, C)

if isDone == False:
    print("끝까지 감")
    print(count)


# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 5
# 8 D
# 2 D
# 1 D
# 2 L
# 8 D

