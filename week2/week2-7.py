# 효율적인 화폐구성
# N : 화폐의 종류
# M : 가치의 합이 M이여야 함
# 각 화폐의 가치가 아래줄에 나타나게 됨
# 불가능하면 -1 리턴
from collections import deque
N, M = map(int, input().split()) # 2, 15
coin = deque()
result = [0] * N
for i in range(N):
    coin.append(int(input()))

for j in range(N):
    x = coin.pop()
    result[j] = M // x
    M = M - x * result[j]
    if M == 0:
        print(sum(result))
        break
if M != 0:
    print(-1)
