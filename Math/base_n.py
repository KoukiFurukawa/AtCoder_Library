def change(num,k):
    num = list(map(int,list(str(num))))[::-1]
    ans = 0
    for i in range(len(num)):
        ans += num[i]*k**i

    res = []
    while ans != 0:
        res.append(ans%k)
        ans //= k
        
    return res
        
