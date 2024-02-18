# dfs, bfs 문제 음료수 얼려먹기
# 0으로 연결된 개수를 구하면 될듯 : bfs 문제인듯 -> dfs로 푸는게 빠름
# 1. 격자에서 0인값을 찾고 카운트 + 1
# 2. x, y 가 있음
# 3. 만약 x, y 의 동서남북값이 격자안이고, false이면서 값이 0이라면 조건합격
# 3-1. 당값을 true로 바꾸고 큐에 넣기

N, M = map(int, input().split())
ice = []
for i in range(N):
    ice.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <- -1 or y >= M:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs[i][j] == True:
            cnt += 1
print(cnt)

                
