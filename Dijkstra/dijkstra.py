from heapq import heappush, heappop
INF = 10**9+7

v,e,r = map(int,input().split()) # （ノード数, エッジ数, 始点ノード）
graph = [[] for _ in range(v)]

for i in range(e):
    s, t, d = map(int, input().split()) # ノード番号、ノード番号、辺重み
    graph[s].append((t, d))

def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in graph[v]: # ノード v に隣接しているノードに対して
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))

    return dist

# debug
d = dijkstra(r, v)
print(d)