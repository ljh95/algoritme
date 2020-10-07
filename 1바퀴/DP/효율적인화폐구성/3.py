n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001]*(m+1)
d[0] = 0
for k in arr:
    for i in range(m+1):
        if d[i-k] != 10001:
            d[i] = min(d[i], d[i-k]+1)

print(d[m])