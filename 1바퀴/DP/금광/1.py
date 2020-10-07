T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    arr = [[0]*m for i in range(n)]
    list_arr = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            k = (i*m)+j
            arr[i][j] = list_arr[k]
    d = [0] * (m+1)
    
    for i in range(1, m):
        d[i] = d[i-1]
        for j in range(n):
            d[i] = max(d[i], arr[j][i-1] + arr[j][i])
            if j != 0:
                d[i] = max(d[i], arr[j-1][i-1] + arr[j][i])
            if j != n-1:
                d[i] = max(d[i], arr[j+1][i-1] + arr[j][i])
            arr[j][i] = d[i]
    print("answer =", d[m-1])
    
