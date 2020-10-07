n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result+=cost
        last = cost

print(result - last)

# 도시를 2개로 분리할 수 있는 개념이 이렇게 쉽게 할 수 있다는 것을 이제 알았다.
# 그러면 3개로 분리하고자 한다면?
# 먼저 last를 동일하게 자르고, second_last를 또 판단할 수 있어야 할까?
# 만약 그렇다면, 그냥 edges를 range로 구분하고 마지막 인덱스의 cost값을 last
# 2번째 마지막 인덱스의 cost값을 secont_last해서 빼면 그만..
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
