from collections import deque

# 連続した要素の条件を満たす範囲の最大を取る
def 尺取り法(lst,k):
    queue = deque()
    cnt = 0
    sum = 0
    res = 0
    for i in lst:
        queue.append(i)
        cnt += 1
        sum += i
        while sum > k: # ここに条件を書く。今回は和がk以下の最大区間を求める
            lf = queue.popleft()
            sum -= lf
            cnt -= 1
        res = max(res,cnt)

    return res