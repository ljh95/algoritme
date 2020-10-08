def make_dfs(graph, start, arr, visited):
    visited[start] = True    
    arr.append(start)
    for i in graph[start]:
        if visited[i] == False:
            make_dfs(graph, i, arr, visited)

arr = []
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

visited = [False] * 9
make_dfs(graph, 1, arr, visited)
print(arr)