# ABC170-F

from collections import *

h,w,k = map(int,input().split())
sx,sy,gx,gy = map(int,input().split())

c = [list(input()) for _ in range(h)]
 
sx,sy,gx,gy = sx-1,sy-1,gx-1,gy-1
visit = [[-1]*w for _ in range(h)] # 上:0 右:1 下:2 左:3

que = deque([[sx,sy]])
visit[sx][sy] = 0

while que:
    x,y = que.popleft()
    for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
        for ml in range(1,k+1):
            nx,ny = x+ml*i, y+ml*j

            if not (0 <= nx < h and 0 <= ny < w and c[nx][ny] != "@"):
                break
            if 0 <= visit[nx][ny] <= visit[x][y]:
                break
            if visit[nx][ny] == -1:
                que.append([nx,ny])
            visit[nx][ny] = visit[x][y] + 1

# print(*visit,sep="\n")
print(visit[gx][gy])