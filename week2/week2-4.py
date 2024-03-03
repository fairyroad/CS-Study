import copy


def turn_left(i):
    if i == 0:
        return 3
    else:
        return i - 1

N, M = map(int, input().split()) # 4, 4
x, y, i = map(int, input().split()) # 1, 1, 0(N)

graph =[]
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = copy.deepcopy(graph) # visited = [[0] * m for _ in range(n)]
stop = 0
dir = ((-1, 0),(0,1),(1,0),(0,-1))
visited[x][y] = 1
cnt = 1

while True:
    nx = x + dir[i][0]
    ny = y + dir[i][1]
    i = turn_left(i)
    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 0:
        x = nx
        y = ny
        visited[x][y] = 1
        cnt += 1
        stop = 0
    else:
        stop += 1
    if stop == 4:
        ny = y - dir[i][1]
        nx = x - dir[i][0]
        if ny >= M or graph[x][y] == 1:
            break
        else:
            y = ny
            x = nx
            stop = 0
print(cnt)  
