# 구현 : 왕실의 나이트
# 나이트는 L자로만 이동함, 정원밖으로는 나갈 수 없음
#     수평으로 두칸 + 수직으로 한칸
#     수직으로 두칸 + 수평으로 한칸
alphabet = ['a','b','c','d','e','f','g','h'] 
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
cur = input()
cur_x = int(alphabet.index(cur[0])) # int(ord(cur[0])) - int(ord(cur['a'])) + 1
cur_y =int(cur[1]) -1
cnt = 0
for i in range(8):
    nx = cur_x + dx[i]
    ny = cur_y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1
print(cnt)
