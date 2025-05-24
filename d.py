a, b = map(int,input().split())
count = 0

while a != b:
    if b > a:
        a, b = b, a
    # print(a, b)
    if b == 0:
        count -= 1
        break
    count += a // b
    a, b = b, a % b

print(count)

