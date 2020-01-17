tc = eval(input())
common = []
for i in range(tc):
    n,m = input().split()
    a1 = input().split()
    b1 = input().split()
    score = 0

    for i in a1:
        if(i in b1):
            score += 1

    common.append(score)


for i in common:
    print(i)
