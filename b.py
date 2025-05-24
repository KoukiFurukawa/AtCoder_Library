s = input()
if s.count("K") == 1 and s.count("Q") == 1 and s.count("R") == 2 and s.count("B") == 2 and s.count("N") == 2:
    cnt = 0
    total = 0
    for i in range(len(s)):
        if s[i] == "R":
            cnt += 1
        if s[i] == "K" and cnt != 1:
            print("No")
            exit()
        if s[i] == "B":
            total += i
    if total % 2 == 0:
        print("No")
        exit()
        
    print("Yes")
else:
    print("No") 