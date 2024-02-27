# greedy 숫자 카드 게임
# 1. 각 N에 대해서 한줄씩 (첫줄, 가장 작은 값) 저장
# 2. 모든 N을 저장한 후 그 중에 가장 큰 값을 return

N, M = map(int, input().split())
x = 0
y = 10000
tmp = []
for i in range(N):
    graph = list(map(int, input().split()))
    tmp.append(min(graph))
print(tmp)
print(max(tmp))
