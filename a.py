a = list(map(int, input().split()))
ans = 0
for i in range(1,5):
    cnt = 0
    for j in a:
        if j == i:
            cnt += 1
    ans += cnt // 2
print(ans)