def solution(n):
    answer = ''
    k=3
    _sum = 3

    while True:
        if _sum > n:
            break
        k*=3
        _sum+=k
    print("_sum: ", _sum)
    return answer

n = 26
print(solution(n))


# print(81//27)