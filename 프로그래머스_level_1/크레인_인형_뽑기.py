def solution(board, moves):
    answer = 0
    arr = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if len(arr) == 0:
                    arr.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
                if arr[-1] != board[i][move-1]:
                    arr.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
                else:
                    arr.pop()
                    board[i][move-1] = 0
                    answer+=2
                    break
    return answer

board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))

# def solution(board, moves):
#     answer = 0
#     n = len(board[0])
#     bucket = []
#     for i in moves:
#         for j in range(n):
#             value = board[j][i-1]
#             if value != 0:
#                 board[j][i-1] = 0
#                 bucket.append(value)
#                 k = len(bucket)-1
#                 if k == 0:
#                     break
#                 if bucket[k] == bucket[k-1]:
#                     del bucket[k]
#                     del bucket[k-1]
#                     answer+=2
#                     break
#                 break
#     return answer