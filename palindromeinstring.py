def palin(s):

    forw = list(s)
    back = list(s)
    back.reverse()

    if (forw == back):
        return True
    else:
        return False

tc = eval(input())
for j in range(tc):
    s = input()
    n = len(s)
    li = []
    size = 0
    for i in range(n-1):

        if(palin(s[i:])):

            size1 = len(s[i:])
#            li.append(s[i:])
            if(size1 > size):

                size = size1
                ans = s[i:]
                print(ans)
        else:
            ans = s[0]

    print(ans)





