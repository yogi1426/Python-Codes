tc = eval(input())
result = []
for i in range(tc):
    n,m,k = input().split()
    n = int(n)
    m = int(m)
    k = int(k)
    minn = min(n,m)
    maxx = max(n,m)

    while (minn<maxx and k>0):

        minn = minn + 1

        k = k - 1
        #print(minn,maxx,k)
    result.append(max(m,n) - minn)

for i in result:
    print(i)
