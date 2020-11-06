n = int(input())
arr = list(map(int, input().split()))

d = [0] * (len(arr)+1)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    d[i] = d[i-2] + arr[i]
    d[i] = max(d[i], d[i-1])

print(d[n-1])