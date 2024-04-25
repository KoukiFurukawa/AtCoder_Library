def gcd(x, y):

    if y > x:
        x,y = y,x
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
    
print(gcd(10101,6105))