def solution(board, moves):
    answer = 0
    n = len(board[0])
    bucket = []
    for i in moves:
        for j in range(n):
            value = board[j][i-1]
            if value != 0:
                print("value= ", value)
                print("j, i", j, i)
                board[j][i-1] = 0
                bucket.append(value)
                k = len(bucket)-1
                if k == 0:
                    break
                if bucket[k] == bucket[k-1]:
                    bucket.remove(bucket[k])
                    bucket.remove(bucket[k-1])
                    answer+=2
                    break
                break
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))