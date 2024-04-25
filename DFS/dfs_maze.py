from collections import deque

def dfs(x,y):
    s = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    stack = deque([[x,y]])
    visited[x][y] = False

    while stack:
        x,y = stack.pop()
        for Q in s:
            nx,ny = x + Q[0], y + Q[1]
            if 0 <= nx < h and 0 <= ny < w and c[nx][ny] == 1 and visited[nx][ny]:
                stack.append([nx,ny])
                visited[nx][ny] = False


while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    c = [list(map(int,input().split())) for _ in range(h)]
    visited = [[True]*w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] and c[i][j] == 1:
                dfs(i,j)
                #print(*visited,sep="\n")
                ans += 1

    print(ans)