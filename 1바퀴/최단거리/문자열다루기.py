def solution(s):
    answer = True
    for i in s:
        if i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '0':
            return False
    return answer

print(solution("1z234"))
