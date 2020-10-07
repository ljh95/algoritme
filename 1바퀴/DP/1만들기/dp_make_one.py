# 내가 쓴 풀이

n = int(input())
count = 0

def make_one(n, count):    
    if n == 1: return count
    one, two, three, five = 9999, 9999, 9999, 9999
    if n % 5 == 0:
        five = make_one(n//5, count + 1)
    if n % 3 == 0:
        three = make_one(n//3 ,count+1)
    if n % 2 == 0:
        two = make_one(n//2, count+1)
    one = make_one(n-1, count+1)
    min_val = min(min(five, three), min(two, one))
    if n == 26:
        print("min_val, ", min_val)
    return min_val

print("answer = ",make_one(n, count))
