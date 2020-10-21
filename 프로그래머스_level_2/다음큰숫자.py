def solution(n):
    answer = 0
    small = bin(n)[2:]
    small_count = 0
    for s in small:
        if s == '1':
            small_count+=1
    n+=1
    while True:
        big = bin(n)[2:]
        big_count = 0
        for s in big:
            if s == '1':
                big_count+=1
        if big_count == small_count:
            answer = n
            break
        else:
            n+=1    
    return answer

n = 15
print(solution(n))
