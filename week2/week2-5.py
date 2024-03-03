# dp 문제 : 개미전사
# 인접하면 바로 알아챔
# 개미 전사는 전략적으로 약탈함 : 최소 한칸 이상 떨어진 식량창고 약탈하기
k = int(input())
N = list(map(int, input().split()))
d = [0] * 100
d[0] = N[0]
d[1] = max(d[0], N[1])
for i in range(2, k):
  d[i] = max(d[i-1], d[i-2] + N[i])
print(d[k-1])
