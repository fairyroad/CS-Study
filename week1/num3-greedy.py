# 그리디 : 큰수의 법칙 p.92
# 배열이 있을때 주어진 수들을 M번 더해서 가장 큰 수를 만드는 법칙
from collections import deque

N, M, K = map(int, input().split())
num = deque(map(int, input().split()))
num_max = sorted(num, reverse=True)
result = 0
for i in range(1, M+1):
    if i % K == 0:
        result = result + num_max[1]
    else:
        result = result + num_max[0]
print(result)
