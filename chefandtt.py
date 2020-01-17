
s = []
n = eval(input())
for i in range(n):
    a = input()
    s.append(a)

for j in s:
    opp_score = 0
    chef_score = 0
    for i in j:
        if(i == '1'):
            chef_score = chef_score + 1
        else:
            opp_score = opp_score + 1
    #print(chef_score, opp_score)
    if(chef_score > opp_score):
        print("WIN")
    elif(chef_score == opp_score):
        if(chef_score == 13):
            print("WIN")
        else:
            print("LOSE")
    else:
        print("LOSE")