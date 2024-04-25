def main():
    from collections import deque

    h,w = map(int,input().split())
    c = [list(input()) for _ in range(h)]

    que = deque([])

    for i in range(h):
        for j in range(w):
            if c[i][j] == "s":
                sx,sy = i,j
            elif c[i][j] == "g":
                gx,gy = i,j

    cost = [[10**9]*w for _ in range(h)]
    cost[sx][sy] = 0

    que.append([sx,sy])

    while que:
        x,y = que.popleft()
        lst = []
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i)+abs(j) != 4 and not(i == 0 and j == 0):
                    lst.append([x+i,y+j])
        for nx,ny in lst:
        # for nx,ny in ([x+1,y],[x,y+1],[x-1,y],[x,y-1]):
            if not (0 <= nx < h and 0 <= ny < w):
                continue

            wall = (c[nx][ny] == "#")
            
            if wall:
                if cost[x][y]+1 < cost[nx][ny]:
                    que.append([nx,ny])
                    cost[nx][ny] = cost[x][y]+1
            else:
                if cost[nx][ny] > cost[x][y]:
                    que.appendleft([nx,ny])
                    cost[nx][ny] = cost[x][y]

    # print(*cost,sep="\n")

    if cost[gx][gy] < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

