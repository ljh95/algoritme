import math

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# print("------------------------------")

print(round(sum(arr) / len(arr)))
arr.sort()
print(arr[len(arr)//2])

dic = dict()
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
max_val = max(dic.values())

drr = []
for i, val in dic.items():
    if val == max_val:
        drr.append(i)

# print("drr =", drr)
if len(drr) > 1:
    print(drr[1])
else:
    print(drr[0])



print(max(arr) - min(arr))