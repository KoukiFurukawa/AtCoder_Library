
import heapq
n, k = map(int,input().split())
a = sorted(list(map(int, input().split())))
ans = [0]
q = [0]
cnt = 0
dic = {}
while len(ans) <= k:
    x = heapq.heappop(q)
    dic[x] = 1
    if ans[cnt] == x:
        for j in range(n):
            t = x + a[j]
            if t not in dic:
                heapq.heappush(q, t)
                dic[t] = 1
    else:
        ans.append(x)
        cnt += 1
        for j in range(n):
            t = x + a[j]
            if t not in dic:
                heapq.heappush(q, t)
                dic[t] = 1
print(ans[k])