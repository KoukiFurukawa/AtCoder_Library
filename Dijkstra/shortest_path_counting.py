from heapq import heappush, heappop

v,e,r = map(int,input().split()) # ノード数、エッジ数、始点
graph = [[] for _ in range(v)]
for _ in range(e):
    a,b,t = map(int,input().split()) # a,bは繋がっており、tがその辺の重み
    graph[a-1].append((b-1,t))
    graph[b-1].append((a-1,t))

cnt = [0]*v # カウントに使う配列
cnt[r] = 1 # 始点は経路の数が1とする
mod = 10**9+7
INF = 10 ** 9

def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n # 始点からの距離を保持
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    # seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        # seen[v] = True
        for to, cost in graph[v]: # ノード v に隣接しているノードに対して
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                cnt[to] = cnt[v]%mod
                heappush(hq, (dist[to], to))
            elif dist[v] + cost == dist[to]:
                cnt[to] += cnt[v]
    return dist

# debug
d = dijkstra(r, v)
print(cnt[v-1]%mod)