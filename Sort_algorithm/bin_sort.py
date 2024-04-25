size = 10
 
def bin_sort(lst):
    bin = [None for _ in range(size)]
    for i in range(len(lst)):
        bin[lst[i]] = lst[i]
    j = 0
    for i in range(size):
        if bin[i]:
            lst[j] = bin[i]
            j += 1
lst = [3,5,8,1,4,2,9]
print(lst)
bin_sort(lst)
print(lst)

# 値の重複は認められない
# 値はある範囲に収まる整数でなければならない
