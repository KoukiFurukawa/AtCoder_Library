def Imos(lst,n):
    """
    lstには処理の開始と終了ポイントが、nには最大の数が入る
    """
    res = [0]*n
    for left,right in lst:
        res[left-1] += 1
        res[right] -= 1

    return res


def 二次元Imos法(lst,h,w):
    """
    lstには左上と右上の点の座標を、h,wには縦横の最大値を入れる
    """
    res = [[0]*w for _ in range(h)]
    for lx,ly,rx,ry in lst:
        res[ly][lx] += 1
        res[ly][rx] -= 1 
        res[ry][lx] -= 1
        res[ry][rx] += 1
    for i in range(h):
        cnt = 0
        for j in range(w):
            cnt += res[i][j]
            res[i][j] = cnt
    for i in range(w):
        cnt = 0
        for j in range(h):
            cnt += res[j][i]
            res[j][i] = cnt

    return res