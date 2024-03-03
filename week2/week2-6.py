# dp 문제: 바닥 공사
# 나머지는 신경쓸 필요없고 맨마지막을 기준으로 1개 남을때, 2개남을때를 생각해보면 됨
# a(n) = a(n-1) + 2*a(n-2)
N = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 2
for i in range(3, N):
    d[i] = (d[i-2] * 2 + d[i-1]) % 796796
print(d[N])