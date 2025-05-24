n = int(input())
p = list(map(float, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n + 1):
    dp[0][i] = dp[0][i - 1] * p[i - 1]
    dp[i][0] = dp[i - 1][0] * (1 - p[i - 1])
    

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j > n:
            break
        dp[i][j] = dp[i-1][j] * (1 - p[i + j - 1]) + dp[i][j - 1] * p[i + j - 1]

ans = 0
for i in range(n + 1):
    for j in range(n + 1):
        if i + j == n and j > i:
            ans += dp[i][j]
print(ans)