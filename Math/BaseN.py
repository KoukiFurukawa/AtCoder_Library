# n進数に変換
def Base_N(n,base):

    ans = []

    while n >= base:
        ans.append(n % base)
        n //= base
    ans.append(n)

    return ans[::-1]