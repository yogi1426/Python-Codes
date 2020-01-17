
def prefixSum(a,i):
    pos = 0
    s = 0
    while(pos <= i):
        s = s + a[pos]
        pos = pos + 1
    #print(s)
    return s

def suffixSum(a,i):
    pos = len(a)-1
    #a.reverse()
    s = 0
    while(i<=pos):
        s = s + a[pos]
        pos = pos - 1
    #print(s)
    return s


arr  = []
tc = eval(input())
for i in range(tc):
    n = eval(input())
    s = input().split()
    b = list(map(int, s))
    arr.append(b)



for a in arr:
    li = []
    for i in range(len(a)):
        summ = prefixSum(a,i) + suffixSum(a,i)
        li.append((summ,i+1))

    li.sort()


    print(li[0][1])