def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]
    i = 0
    idx = [0, 0, n]
    m=1
    while True:
        n-=1
        if i == 0:
            same_col(arr, idx, m)
            m+=idx[2]
            idx[0],idx[1],  idx[2] = idx[0]+n,idx[1]+1, idx[2]-1
            if n == 0:
                break
            i+=1
            continue
        if i == 1:
            same_row(arr, idx, m)
            m+=idx[2]
            idx[0], idx[1], idx[2] = idx[0]-1, idx[1]+n-1, idx[2]-1
            if n == 0:
                break
            i+=1
            continue
        if i == 2:
            both_decrease(arr, idx, m)
            m+=idx[2]
            idx[0], idx[1], idx[2] = idx[0]-n+1, idx[1]-n, idx[2]-1
            if n== 0:
                break
            i-=2
            continue
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0:
                answer.append(arr[i][j])


    return answer
def same_col(arr, idx, n):
    x, y, count = idx
    for i in range(count):
        arr[x+i][y] = n
        n+=1
def same_row(arr, idx, n):
    x, y, count = id
    # print('same_row', idx)
    for i in range(count):
        arr[x][y+i] = n
        n+=1
def both_decrease(arr, idx, n):
    x, y, count = idx
    for i in range(count):
        arr[x-i][y-i] = n
        n+=1


print(solution(6))

