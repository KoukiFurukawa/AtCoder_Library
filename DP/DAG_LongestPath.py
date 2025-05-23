import heapq

n, m = map(int,input().split())
graph = [[] for _ in range(n)]
d = [0] * n
for _ in range(m):
    a, b = map(int,input().split())
    graph[a - 1].append(b -1)
    d[b - 1] += 1 # 向かってくる矢印の数

# 頂点を探す
Q = []
for i in range(n):
    if d[i] == 0:
        heapq.heappush(Q, i)

ans = []
while len(ans) < n:
    # 非巡回グラフの場合、ここで終了する
    if len(Q) == 0:
        break
    x = heapq.heappop(Q)
    ans.append(x)
    for y in graph[x]:
        d[y] -= 1
        if d[y] == 0:
            heapq.heappush(Q, y)
            
# print(*graph, sep="\n")
# print(ans)

dp = [0] * n
for i in range(n):
    node = ans[i]
    for j in graph[node]:
        dp[j] = max(dp[node] + 1, dp[j])

print(max(dp))