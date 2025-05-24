from collections import deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

# DFS
stack = deque([[0,0]])
slide = [[0, 1], [1, 0]]
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1

while stack:
    x,y = stack.popleft()
    for i, j in slide:
        nx, ny = x + i, y + j
        if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == ".":
            if dp[nx][ny] != 0:
                dp[nx][ny] += dp[x][y]
                dp[nx][ny] %= 10**9 + 7
            else:
                dp[nx][ny] = dp[x][y]
                stack.append([nx, ny])
                
print(dp[h-1][w-1] % (10**9 + 7))