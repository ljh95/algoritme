key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
n = len(lock)
m = len(key)

# make huge key arr
huge_key = [[0]*(m + (n-1)*2) for i in range(m + (n-1)*2)]
for i in range(len(huge_key)):    
    for j in range(len(huge_key)):
        if i >= n-1 and i < (m+n-1) and j >= n-1 and j < (m+n-1):
            huge_key[i][j] = key[i-m+1][j-m+1]
print("huge_key : ", huge_key)
print(huge_key[0:3])
# def turn_right():
#     global huge_key
#     temp_arr = [[0]*(m + (n-1)*2) for i in range(m + (n-1)*2)]
#     for i in range(len(huge_key)):
#         for j in range(len(huge_key)):
#             temp_arr[i][j] = huge_key[m-j][i]
#     huge_key = temp_arr
# # print(huge_key)
# for _ in range(4):
#     k_arr =[]
#     for i in range(m+n-1):
#         # for j in range(m+n-1):
#         k_arr.append(huge_key[i][i:i+(n+m-1)])
#         print("ke : ", huge_key[i][i:i+(n+m-1)])
#         print("hu : ", huge_key[i])
#         # print(i , "i+")
#     k_arr = huge_key[i:i+m][j:j+m]
#     flag = True
#     print(k_arr)
#     for a in range(len(lock)):
#         for b in range(len(lock)):
#             if lock[a][b] == k_arr[a][b]:
#                 flag  =False
#     if flag:
#         print("true")
#         break  
#     turn_right()


def solution(key, lock):
    answer = True
    return answer

print("false")