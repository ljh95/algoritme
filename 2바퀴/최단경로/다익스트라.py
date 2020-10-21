import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n. m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드가이미 처리된 적이 있는 ㅗㄴ드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1] # 현재 노드와 연결되 다른 인젖ㅂ한 노드들을 확인
            if cost < distance[i[0]]: # 현재 저장된 거리보다 이번에 발견한 거리의 합이 더 작다면 바꾼다.
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 바꾼 값을 다시 힙에 넣는다.
