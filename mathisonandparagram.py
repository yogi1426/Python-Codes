
n = eval(input())
for i in range(n):
    s = input().split()
    string = input()
    a = list(map(int, s))
    dict1 = {}
    for i in range(len(a)):
        dict1.update({
            chr(i+97) : a[i]
        })


    summ = 0
    for key,value in dict1.items():
        if(key not in string):
            summ = summ + value

    print(summ)