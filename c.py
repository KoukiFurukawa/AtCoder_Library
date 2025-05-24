n  = int(input())
s = input()
ans = 0
for i in s.split("-"):
    ans = max(len(i), ans)
cnt = s.count("-")

if ans != 0 and cnt != 0:
    print(ans)
else:
    print(-1)