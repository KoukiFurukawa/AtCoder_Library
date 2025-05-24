from collections import deque

n, m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a - 1].append(b -1)
    graph[b - 1].append(a -1)
    
k = int(input())
pd = [list(map(int,input().split())) for _ in range(k)]
    
def dfs(node):
    stack = deque([node])
    rg[node][node] = 0
    while stack:
        v = stack.popleft()
        for i in graph[v]:
            t = rg[node][v] + 1
            if rg[node][i] == -1 or t < rg[node][i]:
                stack.append(i)
                rg[node][i] = t
    
rg = [[-1] * n for _ in range(n)]
bw = [1] * n # 1が黒, 0が白
for i in range(n):
    dfs(i)
    

for i in range(k):
    p, d = pd[i]
    p -= 1
    for j in range(n):
        if rg[p][j] < d:
            bw[j] = 0

ok = True
for i in range(k):
    p, d = pd[i]
    p -= 1
    mn = 10 ** 9 + 7
    for j in range(n):
        if bw[j] == 1:
            mn = min(mn, rg[p][j])
    if mn != d:
        ok = False
        break

if ok:
    print("Yes")
    print(*bw, sep="")
else:
    print("No")