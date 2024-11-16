# 島同士が 2R 以内にあればOK
import math

n,r = map(int,input().split())
mp = [[0] * 300 for _ in range(300)]
result = [[0]*300 for _ in range(301)]
ans = [0] * n

graph = [[] for _ in range(n)]

# 150ずつ値を盛る
for i in range(n):
    x,y = map(int,input().split())
    x += 150; y += 150
    mp[x][y] = i+1

# 半径を求める
def solve(d):
    base = (2*r)**2 - d**2
    res = math.sqrt(base)
    return int(res)


def isPath(x,y, root):
    for d in range(2*r+1):
        tr = solve(d)
        for k in range(tr+1):
            if mp[x+d][y+k] != 0:
                graph[root].append(mp[x+d][y+k]-1)
            if mp[x+d][y-k] != 0:
                graph[root].append(mp[x+d][y-k]-1)
            if mp[x-d][y+k] != 0:
                graph[root].append(mp[x-d][y+k]-1)
            if mp[x-d][y-k] != 0:
                graph[root].append(mp[x-d][y-k]-1)
                
def bfs(node):
    stack = [node-1]
    while stack:
        vl = stack.pop()
        visited[vl] = node
        for i in graph[vl]:
            if i == vl or visited[i] != 0:
                continue
            stack.append(i)

for i in range(300):
    for j in range(300):
        if mp[i][j] != 0:
            isPath(i,j,mp[i][j]-1)

visited = [0]*n
for i in range(n):
    if visited[i] == 0:
        bfs(i+1)

print(len(list(set(visited))))