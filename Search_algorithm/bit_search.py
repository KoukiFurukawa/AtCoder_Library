arr = list()
arr = [1,2,3,4,5]

# Bit全探索
def bit_full_search():

    n = len(arr)

    for i in range(2**n):
        bag = []
        for j in range(n):
            if (i >> j) & 1:
                bag.append(arr[j])
            else:
                bag.append(0)

        print(bag)
        
bit_full_search()