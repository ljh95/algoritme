def solution(arr):
    answer = []
    d = [0] * 10
    for i in range(len(arr)):
        if d[arr[i]] == 0:
            d[arr[i]] = 1
            answer.append(arr[i])
        else
    return answer
arr = [1,1,3,3,0,1,1]
print(solution(arr))