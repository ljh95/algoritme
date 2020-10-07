n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in arr:
        if x > mid:
            total += (x - mid)
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)




































arr = sorted(arr, reverse=True) # 10억개를 정렬..?

def add_sum(arr, end, target):
    sum = 0
    for i in arr[:end]:
        sum += i - target
    
    return sum
#          arr  m       0      n-1
def search(arr, target, start, end):
    tmp_sum = 0
    is_left = False
    while start <= end:
        mid = (start + end) // 2
        tmp_sum = add_sum(arr, mid, arr[mid])
        if tmp_sum == target:
            return arr[mid]
        elif tmp_sum > target: # 
            end = mid - 1
            is_left = True
        else:
            start = mid + 1
            is_left = False
    count = 1
    if is_left: # 마지막이 왼쪽값을 확인하고 끝났다면, 떡을 더 짤라야 한다.
        while True:
            tmp_sum += (mid + 1) * count
            if tmp_sum > target:
                return arr[mid] - count
            count += 1
    else:
        while True:
            tmp_sum -= mid * count
            if tmp_sum < target:
                return arr[mid] + count
            count -= 1

print(search(arr, m, 0, n-1))