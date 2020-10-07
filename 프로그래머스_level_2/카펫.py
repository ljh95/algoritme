def solution(brown, yellow):
    answer = []
    _sum = brown + yellow
    for i in range(3, _sum//2):
        if i*i > _sum: break
        if _sum%i == 0:
            count_brown = _sum//i
            count_yellow = i
            d_y = (count_brown-2) * (count_yellow-2)
            d_b = count_brown*count_yellow - d_y
            if d_b == brown and d_y == yellow:
                answer.append(count_brown)
                answer.append(count_yellow)
                break
    return answer

brown = 10
yellow = 2
print(solution(brown, yellow))