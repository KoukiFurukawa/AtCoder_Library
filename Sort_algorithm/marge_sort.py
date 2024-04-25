n = int(input())
a = list(map(int,input().split()))

def MargeSort(lst,left,right):

    if right - left == 1:
        return

    mid = left + (right - left) // 2
    
    MargeSort(lst,left,mid)
    MargeSort(lst,mid,right)

    buf = []
    for i in range(left,mid):
        buf.append(lst[i])
    for j in range(right-1,mid-1,-1):
        buf.append(lst[j])

    iterator_left = 0
    iterator_right = len(buf)-1
    
    for i in range(left,right):
        if buf[iterator_left] <= buf[iterator_right]:
            lst[i] = buf[iterator_left]
            iterator_left += 1
        else:
            lst[i] = buf[iterator_right]
            iterator_right -= 1

MargeSort(a,0,n)
print(*a)