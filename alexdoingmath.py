n = eval(input())
s = input().split()
a = list(map(int, s))

pro = 1
y = 0
for i in a:
    pro = pro * i

a2 = sorted(a)

for i in a2:
    if(i**n > pro):
        y = i
        break
    else:
        continue

print(y)
