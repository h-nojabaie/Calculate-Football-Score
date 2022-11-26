# جمع فوتبالی
# external link:https://quera.org/contest/assignments/44345/problems/148509
n=int(input())
races=[]
for i in range(n):
    r=input().split(" ")
    r2=[int(x) for x in r]
    races.append(r2)
    

for race in races:
    if(race[0]+race[2]>race[1]+race[3]):
        print("perspolis")
    elif(race[0]+race[2]<race[1]+race[3]):
        print("esteghlal")
    else:
        if(race[1]>race[2]):
            print("esteghlal")
        elif(race[1]<race[2]):
            print("perspolis")
        else:
            print("penalty")
