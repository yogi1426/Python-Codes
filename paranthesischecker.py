dict = {
    '{' : '}',
    '(' : ')',
    '[' : ']'
    }
a =  ['{','(','[']
s =  list(input("Enter"))
pos = 0
flag = 0
poslar = s.index(dict.get(s[0]))

for i in range(len(s)):

    if(s[i] in a):

        di = dict.get(s[i])
        pos = s.index(di)
        #print(i,pos,sep = ":")

        if (pos <= poslar):
            if (pos == i + 1 and ((i+1) < len(s)-1 ) ):
                di = dict.get(s[i+2])
                if(di in s[i+1:]):
                    poslar = s[i+1].index(di) + i + 1
                    flag = 1
                else:
                    flag = 0
                    break



            else:
                poslar = pos
                print(pos, poslar, sep=" ")
                flag = 1
                print("flag %s" % flag)

        else:
            print(poslar)
            flag = 0
            print("flag %s" % flag)

print("flag %s" %flag)
if (flag == 0):
    print("Not Balanced")
else:
    print("Balanced")
