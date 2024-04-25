from collections import deque

n = int(input())
graph = deque([deque([]) for _ in range(n)])
for _ in range(n):
    u,k,*v = map(int,input().split())
    for i in range(k):
        graph[u-1].append(v[i]-1)

ans = [-1]*n
ans[0] = 0

def bfs(x):
    while graph[x]:
        q = graph[x].popleft()
        if ans[q] < 0:
            ans[q] = ans[x]+1
        else:
            ans[q] = min(ans[q],ans[x]+1)
        bfs(q)
bfs(0)
    
for i in range(n):
    print(i+1,ans[i])