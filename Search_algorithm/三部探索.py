r,l = 10**36 + 7, -1
while l+2 < r:
    c1 = (l*2+r) // 3
    c2 = (l+r*2) // 3
    
    C1 = cul(c1)
    C2 = cul(c2)
    
    if C1 > C2:
        l = c1
    elif C1 < C2:
        r = c2
    else :
        break