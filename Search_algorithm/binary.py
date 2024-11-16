def binary_search():

    l,r = 0,10**9
    ans = 100

    while r - l > 1:
        mid = (r+l) // 2
        
        if mid > ans:
            r = mid
        else:
            l = mid + 1
    return mid


def binary_select():

    import bisect

    n = [i for i in range(10)]
    print(n)

    # 挿入場所を探索
    left = bisect.bisect_left(n,100)
    print(left)
    # → 2
    right = bisect.bisect_right(n,2)
    # → 3

    # 実際に挿入する
    bisect.insort(n,5)
    # → [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    print(n)
    return left,right

print(binary_select())