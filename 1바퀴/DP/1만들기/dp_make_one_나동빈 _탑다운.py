# import sys
# sys.setrecursionlimit(10000000) #재귀 한도를 늘려준다. RecursionError 방지
# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100000

def solution(n):
    if d[n] != 0 or n == 1:
        return d[n]
    
    d[n] = solution(n-1)+1
    if n % 2 == 0:
        d[n] = min(solution(n//2)+1, d[n])
    if n % 3 == 0:
        d[n] = min(d[n], solution(n//3)+1)
    if n % 5 == 0:
        d[n] = min(d[n], solution(n//5)+1)    
    return d[n]

print(solution(x))


# # 다이나믹 프로그래밍 진행(보텀업)
# for i in range(2, x + 1):
#     # 현재 수에서 1을 빼는 경우
#     d[i] = d[i - 1] + 1
#     # 현재의 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     # 현재의 수가 3으로 나누어 떨어지는 경우
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
#     # 현재의 수가 5로 나누어 떨어지는 경우
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5]+1)

# print(d[x])