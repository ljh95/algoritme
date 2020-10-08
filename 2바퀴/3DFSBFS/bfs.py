from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False]*9
def make_bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
make_bfs(graph, 1, visited)