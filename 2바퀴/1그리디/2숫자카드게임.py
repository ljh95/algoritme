n, m = map(int, input().split())
arr = []
for i in range(n):
    temp_arr = list(map(int, input().split()))
    arr.append(min(temp_arr))

print(max(arr))

# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 예시
# 2
# 3