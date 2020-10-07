import heapq
import sys
input = sys.stdin.readline


INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
max_value = 0
count = 0
for d in distance:
    if d != INF:
        count+=1
        max_value = max(d, max_value)
print(count - 1, max_value)