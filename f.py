def cal_sec(num) -> str:
    sec = (num // 12 + 1) * 90
    res = f"~ {sec // 60} 分 {sec % 60} 秒"
    return res

s = cal_sec(24)
print(s)