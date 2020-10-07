def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

# 서로소 트리의 집합 형태를 보자
print("서로소 집합의 구조: ", end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

# 각 노드의 부모들을 보자.
print("각 노드의 부모: ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
