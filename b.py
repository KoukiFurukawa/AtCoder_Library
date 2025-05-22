h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]

def shift(y, x):
    result = [[0] *w for _ in range(h)]
    # 縦シフト
    for i in range(h):
        for j in range(w):
            result[(i+y) % h][(j+x) % w] = a[i][j]

    return result == b

for i in range(h):
    for j in range(w):
        if shift(i, j):
            print("Yes")
            exit()
print("No")