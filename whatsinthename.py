n = eval(input())

for i in range(n):
    s = input().lower().split()
    initials = ""
    for i in range(len(s)-1):
        initials = initials + s[i][0] + "." + " "
        initials = initials.upper()

    last = s[len(s)-1]
    last = last[0].upper() + last[1:]
    print(initials + last)