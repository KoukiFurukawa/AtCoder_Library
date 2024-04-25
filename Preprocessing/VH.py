arr = [[i for i in range(5)] for j in range(5)]
h,w = 5,5

def VH_Preprocessing():

    #行の計算
    V = [sum(row) for row in arr]
    #列の計算
    H = [sum(col) for col in zip(*arr)]

    dist = [[V[i]+H[j]-arr[i][j] for j in range(w)] for i in range(h)]

    return dist