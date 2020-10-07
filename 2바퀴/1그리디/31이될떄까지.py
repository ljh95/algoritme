n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n//=k
        count+=1
    else:
        n-=1
        count+=1
print(count)

# 입력 예시
# 17 4
# 25 5

# 출력 예시
# 3
# 2