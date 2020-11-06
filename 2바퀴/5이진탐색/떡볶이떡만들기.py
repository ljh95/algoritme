n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
count  = 0
while start<= end:
    mid = (start + end) // 2
    result = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            result += (arr[i] - mid)
    
    if result >= k:
        count = mid
        start = mid + 1
    else:
        end = mid - 1
print(count)
