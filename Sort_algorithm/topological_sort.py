# 条件をつけた上でソート

def topological_sort():
    import heapq

    d = []
    # d = deque([i for i in range(n) if deg[i] == 0])

    # 入力によって n　に変える
    for i in range(1,n+1):
        if deg[i] == 0:
            heapq.heappush(d,i)
            # d.append(i)

    order = []
    while d:
        v = heapq.heappop(d)
        # v = d.popleft()
        order.append(v)
        for v2 in outs[v]:
            deg[v2] -= 1
            if deg[v2] == 0:
                heapq.heappush(d,v2)
                # d.append(v2)
    return order

from collections import defaultdict,deque

n,m = map(int,input().split())
outs = defaultdict(list)
deg = defaultdict(int)

for _ in range(m):
    a,b = map(int,input().split())
    outs[a].append(b)
    deg[b] += 1