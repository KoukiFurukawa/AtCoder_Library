def Cumulative_sum():

    dist = [0]
    num = [i for i in range(10)]

    for i in num:
        dist.append(dist[-1]+i)

    return dist