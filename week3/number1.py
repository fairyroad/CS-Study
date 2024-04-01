# 다익스트라 알고리즘 : 최단거리(greedy 유형)
# input = sys.stdin.readline으로 하면 조금 더 빠르게 입력받기 가능
# 모든 리스트는 N + 1로 해서 인덱스 그대로 접근 할 수 있게 하기
# heapq를 사용해서 조금 더 빠르게 풀수 있음

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input()) # 시작하는 노드
graph = [[]* m for _ in range(n+1)]
distance = [INF] * (m+1)

for _ in range(n):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < INF: # 처리된적 있는 노드
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
