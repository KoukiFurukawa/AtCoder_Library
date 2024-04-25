# ユークリッドの互除法
# エラトステネスの篩↑ なんのミス？？？

def primes(n):
    judgment = [True]*(n+1)
    judgment[0] = False
    judgment[1] = False

    for i in range(n+1):
        if not judgment[i]:
            continue
        for j in range(i*2,n+1,i):
            judgment[j] = False

    res = []
    for i in range(n+1):
        if judgment[i]:
            res.append(i)

    return res

print(primes(int(1000000000**0.5)+1))