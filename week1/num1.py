# 문제 : https://www.acmicpc.net/problem/20055
# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
#   로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

# 내구도 = durability
from collections import deque

def rotate_conv():
    N, K = map(int, input().split())
    durability = deque(list(map(int, input().split())))
    conv = deque([False] *(2*N))

    num = 1
    while True:
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        conv.rotate()
        durability.rotate()
        for i in range(N-1, -1 , -1):
            conv[N-1] = False
            if i == 0 and durability[0] != 0: #올리는 위치
                conv[0] = True
                durability[0] = durability[0] - 1
            #로봇이동
            elif conv[i] == True and conv[i+1] == False and durability[i+1] >= 1:
                conv[i+1] = True
                conv[i] = False
                durability[i+1] = durability[i+1] - 1           
            if durability.count(0) >= K:
                return num 
        num = num + 1

print(rotate_conv())

