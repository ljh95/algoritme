n = int(input())
arr = [[0]*n for _ in range(n)]
for i in range(n): 
    arr[i] = list(map(int, input().split()))
d = [0] * n
for i in range(1, n):
    d[i] = d[i-1] + arr[i-1][0]
    for j in range(i+1):
        d[i] = max(d[i], (d[i-1] + arr[i][j]))

print(d[n-1])

# ex)
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
#