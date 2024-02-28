def turn_left(i):
    if i == 0:
        return 3
    else:
        return i - 1
N, M = map(int, input().split())
x, y, i = map(int, input().split())
graph =[]
for _ in range(N):
    graph.append(list(map(int, input().split())))
cnt = 0
stop = 0
dir = ((0,-1),(-1,0),(0,1),(1,0))
print("================================================")
print(x, y)
while True:
    nx = x + dir[i][0]
    ny = y + dir[i][1]
    print(nx, ny)
    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
        i = turn_left(i)
        print("direction changed:", i)
        x = nx
        y = ny
        graph[x][y] = 0
        cnt += 1
        stop = 0
        print("current location:", x, y)
        print("current count:", cnt)
    else:
        i = turn_left(i)
        stop += 1
        print("oops there's no available move. direction changed", i)
    if stop == 4:
        y = ny + 1
        x = nx
        stop = 0
        print("too many stops")
        if ny >= M or graph[x][y] == 0:
            print("ALL STOP")
            break
print(cnt)        
