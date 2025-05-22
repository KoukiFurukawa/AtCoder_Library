n = int(input())
h = list(map(int,input().split()))
t = 0
ans = 0

for i in range(n):
    hp = h[i]
    if hp % 5 == 0:
        ans += hp // 5 * 3
    else:
        shape = t % 3
        if shape != 0:
            shape = 3 - shape
            if shape == 1:
                hp -= 3
                ans += 1
                t += 1
                if hp <= 0:
                    continue
            if shape == 2:
                if hp == 1:
                    ans += 1
                    t += 1
                    continue
                hp -= 4
                ans += 2
                t += 2
                if hp <= 0:
                    continue
        # print(shape)
        
        if 0 <= hp % 5 < 3:
            ans += hp // 5 * 3 + hp % 5
            t += hp % 5
        else:
            ans += hp // 5 * 3 + 3
            
    t %= 3
#     print(ans)

# cnt = 0
# t2 = 0
# while h:
#     t2 += 1
#     h[0] -= 1 if t2 % 3 != 0 else 3
#     if h[0] <= 0:
#         h.pop(0)
#     cnt += 1

print(ans)