n = int(input())
s = input()

cnt = 0
for i in range(n):
    if s[i] == "|":
        cnt += 1
    if cnt == 1 and s[i] =="*":
        print("in")
        exit()
        
print("out")