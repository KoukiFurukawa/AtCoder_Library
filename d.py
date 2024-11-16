from collections import deque

h, w, k = map(int,input().split())
s = [input() for _ in range(h)]
ans = 0

def CountRoot(y, x):
    res = 0
    slide = [[0,1],[0,-1],[1,0],[-1,0]]
    board = [[[0]*w for _ in range(h)] for _ in range(k+1)]
    stack = deque([(y, x, 0, [(y * w + x)])])
    board[0][y][x] = 1
    while stack:
        y, x, t, r = stack.popleft()
        # print(y, x, t, r)
        if t == k:
            continue
        for i, j in slide:
            nx, ny = x + i, y + j
            if 0 <= nx < w and 0 <= ny < h and s[ny][nx] == "." and ny * w + nx not in r:
                board[t + 1][ny][nx] += 1
                nr = r.copy()
                nr.append(ny * w + nx)
                stack.append((ny, nx, t + 1, nr))
                
    for i in range(h):
        for j in range(w):
            if board[k][i][j] != -1:
                res += board[k][i][j]
                
    # for i in range(k+1):
    #     print(board[i][0])
    #     print(board[i][1])
    #     print()
    # print()
    return res

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            ans += CountRoot(i, j)

print(ans)