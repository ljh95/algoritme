# 솔루션
# 1) M*2 + N 크기의 보드를 만들고 중앙에 좌물쇠를 바치한다.
# 2) key를 4번 돌려가며 차례로 이동시킨다.
# 3) 위에어 아래로 열쇠를 이동했을때 중앙의 키가 모두 1이 되면 unlock
# def rotate90
# def attach 열쇠 넣어보기
# def detach 열쇠 빼기
# def check 모두 1인지 확인

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    # test = list(zip(*arr[::-1]))
    mk_arr = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            mk_arr[i][j] = arr[2-j][i]
    # print("test: ", test)
    # print("mk_arr:", mk_arr)
    return mk_arr

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]

    #자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    print(board)
    rotated_key = key
    # 모든 방향(4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if (check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))