n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
def dfs(graph, i, j):
    if i <= -1 or i > n-1 or j <= -1 or j > m-1:
        return    
    if graph[i][j] == 1:
        return
    graph[i][j] = 1    
    dfs(graph, i-1, j)
    dfs(graph, i+1, j)
    dfs(graph, i, j-1)
    dfs(graph, i, j+1)


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result+=1
            dfs(graph, i, j)

print(result)