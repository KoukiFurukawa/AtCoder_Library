import itertools

# 組み合わせの数
def combinations():

    dist = list(itertools.combinations(range(5),3))

    return dist

# 並べ方
def permutations():

    dist = list(itertools.permutations(range(5),3))

    return dist

# デカルト積
def product():

    number = [(i,j) for i in range(3) for j in range(3,6)]
    dist = itertools.product(*number)

    return dist