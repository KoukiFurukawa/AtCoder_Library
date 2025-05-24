n = int(input())

left = 0
right = n - 1

# left と right が隣り合うまでループ (right - left > 1)
while right - left > 1:
    mid = left + (right - left) // 2
    # インタラクティブ問題では、クエリするインデックスは1-basedが多いので mid + 1 を使用
    print(f"? {mid + 1}", flush=True)
    s_mid_val = int(input())

    if s_mid_val == 0: # S[left] の値は0と仮定
        left = mid
    else:
        right = mid

print(f"! {left + 1}", flush=True)

"例 : n = 5, s = 00101"
"例2: n = 6, s = 010101"