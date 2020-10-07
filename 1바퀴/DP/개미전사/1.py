n = int(input())
arr = list(map(int, input().split()))

d = [0] * (n+2)
d[0] = arr[0]
d[1] = max(arr[1], arr[0])

def dp(i):
    if i < 2:
        return d[i]
    d[i] = max(dp(i-1), dp(i-2) + arr[i])
    return d[i]


answer = dp(n)
print(answer)