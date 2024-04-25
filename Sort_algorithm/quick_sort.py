from collections import deque
from random import randint
import time
import sys

sys.setrecursionlimit(10**9)

def create_random_lst():
    lst = []
    for _ in range(10**6):
        lst.append(randint(0,10**9+7))
        
    return lst
        
def QuickSort(lst):
    
    if len(lst) <= 1:
        return lst
    
    left,right = [],[]
    # 普通のクイックソート
    pivot = lst[len(lst)//2]
    # 乱択クイックソート
    # pivot = lst[randint(0,len(lst)-1)]
    pivot_cnt = 0
    
    for i in lst:
        if i == pivot:
            pivot_cnt += 1
        elif i > pivot:
            right.append(i)
        else:
            left.append(i)
    
    return QuickSort(left) + [pivot]*pivot_cnt + QuickSort(right)


def QuickSort_Stack(lst):
    
    stack = deque([])
    
    
    return 0

for i in range(10):
    lst = create_random_lst()
    ans = time.time()
    QuickSort(lst)
    print(time.time()-ans)