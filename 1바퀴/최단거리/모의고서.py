def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a, b, c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            a+=1
        if answers[i] == two[i%len(two)]:
            b+=1
        if answers[i] == three[i%len(three)]:
            c+=1
    max_value = max(max(a, b), c)
    arr = [a, b, c]
    for i in range(len(arr)):
        if arr[i] == max_value:
            answer.append(i+1)
    return answer
answers = [1,3,2,4,2]

print(solution(answers))