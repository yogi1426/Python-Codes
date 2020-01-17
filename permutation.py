from itertools import permutations

n = eval(input())
s = []
for i in range(n):
    s.append(input())

stri=""
for i in s:
    perm = list(permutations(i))
    for j in perm:
        stri  = stri + "".join(j) + " "
    print(stri.rstrip())

