from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**9)

n = int(input())
graph = deque([deque([]) for _ in range(n)])

for i in range(n):
    u,k,*v = map(int,input().split())
    v = sorted(v)
    graph[u-1] = deque(v)

arrive_time = [-1]*n
finish_time = [-1]*n
time = 0

def dfs(v):
    global time
    time += 1
    if arrive_time[v] < 0:
        arrive_time[v] = time
    else:
        time -= 1
        return
    while graph[v]:
        dfs(graph[v].popleft()-1)
    time += 1
    finish_time[v] = time


for i in range(n):
    dfs(i)

for i in range(n):
    print(i+1,arrive_time[i],finish_time[i])



INF = 10**9+7
visited = [INF]*n

def dfs(v,time):
    if visited[v] == INF:
        visited[v] = min(time,visited[v])
        for i in graph[v]:
            dfs(i,time+1)
    else:
        visited[v] = min(time,visited[v])