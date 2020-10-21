n, m = map(int, input().split())
max_value= 0
for _ in range(n):
    arr = list(map(int, input().split()))
    min_in_column = min(arr)
    if min_in_column > max_value:
        max_value = min_in_column

print(max_value)