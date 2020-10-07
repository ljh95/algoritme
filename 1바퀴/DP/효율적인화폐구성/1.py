n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [99999] * 99999
d[0] = 0
for i in range(1, m+1):
    for k in arr:
        if d[i-k] != 99999:
            d[i] = min(d[i], d[i-k] + 1)

if d[m] == 99999:
    print(-1)
else:
    print(d[m])