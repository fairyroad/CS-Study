# bfs 미로 탈출 : p.152
from collections import deque
N, M = map(int, input().split())

#2차원 미로 정보 입력받기
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

queue=deque()
queue.append((0,0))
while queue:
        x, y = queue.popleft()
        if graph[x][y] != 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
print(graph[N-1][M-1])
