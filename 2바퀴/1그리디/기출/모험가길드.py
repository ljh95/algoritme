n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

i = 0
count = 0

while True:
    if i >= len(arr): break
    max_value = arr[i]
    arr_len = len(arr[i:])

    if max_value <= arr_len:
        i += max_value
        count+=1
    else:
        break

print("result =", count)    