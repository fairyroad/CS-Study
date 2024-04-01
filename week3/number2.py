#플로이드 워셜 알고리즘으로 풀수 있음
#다익스트라는 그리디 알고리즘으로 어떤 특정지점에서 특정지점으로 가는 최단거리를 구한다면, 
#플로이드 워셜은 dp 알고리즘으로 모든 지점에서 모든 지점으로 가는 최단거리를 구하는 문제에 적합함
import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input()) #노드의 개수
m = int(input()) #간선의 개수
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
    graph[i][i] = 0

#이미 간선에 있는 친구들 적어두기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#dp 사용에서 최단거리 계산
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n+1):
    for b in range(b+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
