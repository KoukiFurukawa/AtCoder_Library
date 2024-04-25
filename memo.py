# 入力受け取り高速化
import sys
input = lambda: sys.stdin.readline().rstrip()


# アルファベット生成
alphabet = [chr(i) for i in range(97, 97+26)] # 小文字
alphabet = [chr(i) for i in range(65, 65+26)] # 大文字


# 同じ数を違う値として扱いたい時
a = (2<<18)+1
b = (2 << 18)+2
print(a,b) # 524289 524290
print(a>>18,b>>18) # 2 2


# 再帰回数の上限
import sys
sys.setrecursionlimit(10**7)


# 優先順位付きでソート
a = [[1,2],[1,1],[2,1]]
sorted(a) # [[1, 1], [1, 2], [2, 1]]
sorted(a, key=lambda x:x[1]) # [[1, 1], [2, 1], [1, 2]]

# 以下のように x:(...) とカッコの中に2つ以上条件を入れられる。
# 要素に - （←マイナス）を挿れることによって、逆順にソートできる
sorted(a,key=lambda x:(-x[1],x[0])) # [[1, 2], [1, 1], [2, 1]]
# なお、条件付きソートはトポロジカルソートというものもある。


# 値をコピー。参照元を変えたりする
from copy import *
a = 0
a = copy(a)
a = [[1,1]]
A = deepcopy(a)
(id(a) == id(A)) # False


# ビット全探索を使わずに組み合わせを全列挙
A = [1,2,3]
L = [0]
for x in A[:20]:
    for i in range(len(L)):
        L.append(x + L[i])
print(L)


# modの割り算をするとき
n = 10;r = 5 # nCr
mod = 10**9+7
def mod_comb(n,r,mod):
    p,q = 1,1 # p/q%modとする
    for i in range(r):
        p = p*(n-i)%mod # 上辺のmod
        q = q*(i+1)%mod # 下辺のmod
    q = pow(q,mod-2,mod)
    """
    フェルマーの小定理より、q**(mod-1) % mod = 1
    q * q**(mod-2) % mod = 1
    q**(mod-2)%mod = q**(-1) = 1/q
    modの世界では直接求めるよりも、q**(mod-2)%modした方が良さそう
    """
    return p*q%mod
    
    
# 回文判定
s = "akaaka"
if s[:len(s)//2] == s[len(s)//2:len(s)]:
    print("Yes")
    
# 横に回す
a = [
    [1,2,3],
    [4,5,6]
]
print(list(zip(*a)))