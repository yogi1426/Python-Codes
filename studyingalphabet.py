from itertools import  permutations

read = input()
n  = eval(input())
perm = list(permutations(read))
permu =[]
for j in perm:
    permu.append("".join(j))
string = []
for  i in range(n):
    string.append(input())

for string1 in string:
    if(string1 in permu):
        print("Yes")
    else:
        print("No")
