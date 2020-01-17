tc = eval(input())
for i in range(tc):
    s = input().split()
    a  = list(map(int,s))
    count_1 = a.count(1)
    count_0 = a.count(0)
    if(count_0 < count_1 and count_0 > 0):

        a[a.index(0)] = 1
        count_0 = count_0 - 1
        count_1 = count_1 + 1
    elif(count_1 < count_0 and count_1 > 0):
        a[a.index(1)] = 0
        count_1 = count_1 - 1
        count_0 = count_0 + 1

    #print(a)
    if(count_0 == len(a) or count_1 == len(a) ):
        print("Yes")
    else:
        print("No")

