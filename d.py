n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

v = list(map(int, input().split()))
visited = [[-1, -1]]*n
dic = {}

def bfs(node):
    stack = [node]
    visited[node] = [0, -1]
    while stack:
        vl = stack.pop()
        for i in graph[vl]:
            if visited[i][0] == -1:
                stack.append(i)
                visited[i] = [visited[vl][0] + 1, vl]

bfs(v[0]-1)

print(visited)