# 1이 될때 까지
# N이 1이 될때가지 두 과정 중 하나를 반복적으로 선택함
# 1. N = N - 1
# 2. N % K == 0 이라면 N = N // K
N, K = map(int, input().split())
cnt = 0
while N != 1:
    if N % K == 0 :
        N = N // K
    else:
        N = N - 1
    cnt += 1
print(cnt)
