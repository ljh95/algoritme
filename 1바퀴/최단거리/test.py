def solution(board, moves):
    answer = 0
    bucket = []
    for i in moves:
        for j in range(len(board[i-1])-1, -1, -1):
            if board[j][i-1] != 0:
                temp = board[i-1][j]
                # print("temp", temp)
                board[i-1][j] = 0
                if len(bucket) == 0:
                    bucket.append(temp)                    
                    continue
                
                if bucket[len(bucket)-1] == j:
                    del bucket[len(bucket)-1] 
                                                
                    answer+=2
                    continue
                bucket.append(temp)
                print(bucket)  
                
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = 	[1,5,3,5,1,2,1,4]

print(solution(board, moves))