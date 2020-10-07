from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    if arr[0] == 1:
        print(2) 
    else: print(1) 
else:
    temp_set = set(arr)
    temp_set.add(sum(arr))
    for i in range(2, len(arr)):    
        for j in list(combinations(arr, i)):
            temp_set.add(sum(j))
    temp_set = list(temp_set)
    for i in range(1, len(temp_set)):
        if i not in temp_set:
            print(i)
            break