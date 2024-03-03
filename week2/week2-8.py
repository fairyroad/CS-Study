# dfs + dp 문제 풀이방법
# 사회망 서비스 : https://www.acmicpc.net/problem/2533
# 문제 답을 봤음 
import sys
sys.setrecursionlimit(10 ** 9) # 이건 기억하기
input = sys.stdin.readline # 이것도 아마 메모리를 줄여줄 수동..? 기억해두기

def dfs(v):
    visited[v]=True #방문처리
    for next in adj[v]: #인접한 노드 방문
        if(visited[next]): continue #방문했다면 넘어가기
        dfs(next) #인접한 다음 노드 dfs
        dp[v][0]+=dp[next][1] #내가 얼리얼답터가 아니면 자식노드가 얼리어답터여야해
        dp[v][1]+=min(dp[next]) #내가 얼리얼답터면 자식노드가 뭐든 상관 없어 : 내가 생각할 때는 dp[next][0] 인줄 알았는데 상관없는게 맞음!!!!


N = int(input())
adj = [[] for _ in range(N+1)]
visited=[False]*(N+1)

dp= [[0,1] for _ in range(N+1)]

for i in range(N-1):
    f,t=map(int,input().split())
    adj[f].append(t)
    adj[t].append(f)

dfs(1) #아무 노드에서 시작해도 상관없음
print(min(dp[1]))
