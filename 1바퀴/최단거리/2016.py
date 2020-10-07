def solution(a, b):
    answer = ''
    d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    val = 0
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 10 or i == 12:
            val += 31
        elif i == 4 or i == 6 or i == 8 or i == 11:
            val += 30
        else:
            val += 29
    val+=b
    print("val = ", val)
    answer = d[val%7]
    print(answer)
    return answer
solution(5, 24)