n, k = map(int, input().split())
namuge = n%k
count = 0
count += namuge
n -= namuge
count += n//k
print(count)