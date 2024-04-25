import itertools

k = int(input())
C = [["."]*8 for _ in range(8)]
ches = [-1]*8
for _ in range(k):
    x,y = map(int,input().split())
    ches[x] = y

dist = list(itertools.permutations(range(8),8))

def solve(sample):
    if len(sample) != len(list(set(sample))):
        return False
    else:
        for i in range(8):
            for j in range(8):
                if i == j:
                    continue
                if sample[i]+i == sample[j]+j or sample[i]-i == sample[j]-j:
                    return False
    return True

for sample in dist:
    Do = True
    for check in range(8):
        if ches[check] == -1:
            continue
        else:
            if sample[check] != ches[check]:
                Do = False
                break
    if Do:
        if solve(sample):
            for i in range(8):
                C[i][sample[i]] = "Q"
                print(*C[i],sep="")
            exit()