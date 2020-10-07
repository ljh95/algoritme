n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
a, b = arr[0], arr[1]
print("a, b = ", a, b)

moc = m//(k+1)
namuge = m%(k+1)
result = moc*(a*k + b) + namuge*a
print("result =", result)

# 예시 입력
# 5 8 3
# 2 4 5 4 6

# 예시 출력
# 46