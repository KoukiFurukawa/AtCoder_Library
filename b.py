n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

t_cnt = c.count(t)

if t_cnt == 0:
    t = c[0]

mx = -1
ans = 0
for i in range(n):
    if c[i] == t:
        if mx < r[i]:
            ans = i + 1
            mx = r[i]
            
print(ans)