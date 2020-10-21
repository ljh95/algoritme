n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
# 이 부분을 굳이 정렬하지 않아도 최댓값 2개만 찾으면 되므로 좀 더 단축 시킬 수도 있을 것이다.

first = arr[-1]
second = arr[-2]

quotient = m // (k+1)
rest = m % (k+1)

answer = quotient * (first*k + second) + second*rest
print(answer)
