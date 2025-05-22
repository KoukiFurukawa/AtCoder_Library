n, W = map(int,input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [-1] * (W + 1) # 価値 n を実現するための最小Weight
dp[0] = 0
for i in range(n):
    w, v = wv[i]
    for j in range(W, -1, -1):
        if dp[j - w] != -1 and j - w >= 0:
            dp[j] = max(dp[j], dp[j - w] + v)

print(max(dp))


