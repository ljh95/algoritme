import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
count = 0
max_value = 0
for d in distance:
    if d == INF:
        continue
    else:
        count+=1
        max_value = max(max_value, d)
print(count-1, max_value)

# 3 2 1
# 1 2 4
# 1 3 2
