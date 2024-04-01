#전보
import heapq
import sys

INF = int(1e9)
input = sys.stdin. readline

N, M, start = map(int, input().split())
graph= [[] for _ in range(N+1)]
distance = [INF] * (M+1)

for _ in range(M):
    x,y,z = map(int, input().split())
    graph.append(x,(y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop()
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d!=INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance) # 시작 제외
