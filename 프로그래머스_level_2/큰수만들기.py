from collections import deque

def solution(number, k):
    answer = ''
    n = len(number)
    pos = n-k
    q = deque()
    q.append(int(number[0]))
    idx = 0
    for i in range(1, len(number)):
        if len(number[i:])+len(q) < pos:
            idx = i
            break
        while q:
            top = q.pop()
            if int(top) >= int(number[i]):
                q.append(top)
                q.append(int(number[i]))
                # pos-=1
                break
            # else: pos+=1
        if len(q) == 0: q.append(int(number[i]))
    print()
    print(q)
    print(number[idx:])
    for i in q:
        answer+=str(i)

    answer+=number[idx:]
    return answer

number = '4177252841'
k = 4
print(solution(number, k))