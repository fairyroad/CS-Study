#구현, 오리
duckSound = list(input())
lenDuck = len(duckSound)
visited = [False] * lenDuck
duck = ['q','u','a','c','k']
result = 0

# while visited.count(False) != 0:
#     check = 0
#     idx = 0
#     for i in duck:
#         for j in range(idx, lenDuck):
#             if visited[j] == False and i == duckSound[j]:
#                 visited[j] = True
#                 check += 1
#                 idx = j+1
#                 break
#     if check == 5:
#         result += 1

# if result != duckSound.count('q'):
#     print(-1)
# else:
#     print(result)

def findDuck(idx):
    loc = idx
    check = 0
    for k in duck:
        for j in range(loc, lenDuck):
            if visited[j] == False and k == duckSound[j]:
                visited[j] = True
                check += 1
                loc = j+1
                break
    if check == 5:
        return True, loc
    return False, loc

while True:
    for i in range(lenDuck):
        if duckSound[i] == 'q':
            before = False
            duck = i
            for idx in range(duck, lenDuck):
                if duckSound[idx] == 'q':
                    print(idx)
                    flag, duck = findDuck(idx)
                    if before == True:
                        continue
                    elif flag == True:
                        result += 1
    if visited.count(False) != 0:
        print(-1)
    else:
        print(result)
    break
