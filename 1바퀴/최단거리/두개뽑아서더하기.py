def solution(numbers):
    answer = []
    set1 = set([])
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            set1.add(numbers[i]+numbers[j])
    answer = list(set1)
    return answer
numbers = [2,1,3,4,1]
print(solution(numbers))