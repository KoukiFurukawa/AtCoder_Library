S = input()
T = input()

# LCS
def LCS(s,t):
    
    dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s) + 1):
        dp[i][0] = 0
    for j in range(len(t) + 1):
        dp[0][j] = 0
        
    def isSame(x, y) -> int:
        return 1 if x == y else 0
        
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            dp[i][j] = max(dp[i-1][j-1] + isSame(s[i-1], t[j-1]), dp[i][j-1], dp[i-1][j])

    return dp

# LCSの長さを取得 (dpテーブルの右下)
dp_table = LCS(S, T)
# 文字列復元
i = len(S)
j = len(T)
lcs_str = ""
while i > 0 and j > 0:
    # s[i-1]とt[j-1]が一致する場合、LCSに含めて左上に移動
    if S[i-1] == T[j-1]:
        lcs_str = S[i-1] + lcs_str
        i -= 1
        j -= 1
    # dp[i-1][j]の方が大きい場合、上に移動
    elif dp_table[i-1][j] > dp_table[i][j-1]:
        i -= 1
    # dp[i][j-1]の方が大きい（または等しい）場合、左に移動
    else:
        j -= 1

print(lcs_str)