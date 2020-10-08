from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    start, end = map(int, input().split())    
    graph[start-1].append(end)

visited = [False] * (n+1)
q = deque()
arr = []
def bfs(x):
    q.append((x, 0))
    visited[x] = True

    while q:
        x, count = q.popleft()
        arr.append((x, count))
        
        for i in graph[x-1]:
            if visited[i] == False:
                visited[i] = True
                q.append((i, count+1))

bfs(x)
arr.sort()
flag = False
for i, count in arr:
    if count == k:
        flag = True
        print(i)

if flag == False:
    print(-1)