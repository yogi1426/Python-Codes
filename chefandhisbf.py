def check(a):
    counter = 0
    for i in range(leng - 1):
        temp = 0
        if (a[i] == 0 and a[i + 1] == 1):
            counter = counter + 1
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
    #print(a)
    return counter

n = eval(input())
result = []
counter = 0
for j in range(n):
    leng = eval(input())
    s = input().split()
    a = list(map(int, s))
    counter += check(a)

print(counter)

