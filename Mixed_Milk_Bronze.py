#https://usaco.org/index.php?page=viewproblem2&cpid=855

maxMilk = [] #Add inputs later
amt = [] #Add inputs later
pourNum = 0
numMilk = 3
amtNum = 3
while numMilk > 0:
    milk = int(input())
    maxMilk.append(milk)
    numMilk -= 1

while amtNum > 0:
    bob = int(input())
    amt.append(bob)
    amtNum -= 1

while pourNum < 100:
    if pourNum % 3 == 0:
        if amt[0] + amt[1] <= maxMilk[1]:
            amt[1] = amt[0] + amt[1]
            amt[0] = 0
            print(amt[1])
        else:
            amt[1] = maxMilk[1]
            amt[0] = amt[0] - maxMilk[1]
            print(amt[1])
    #pourNum += 1
    if pourNum % 3 == 1:
        if amt[1] + amt[2] <= maxMilk[2]:
            amt[2] = amt[1] + amt[2]
            amt[1] = 0
            print(amt[2])
        else:
            amt[2] = maxMilk[2]
            amt[1] = amt[1] - maxMilk[2]
            print(amt[2])
    
    if pourNum % 3 == 2:
        if amt[2] + amt[0] <= maxMilk[0]:
            amt[0] = amt[0] + amt[2]
            amt[2] = 0
            print(amt[0])
        else:
            amt[0] = maxMilk[0]
            amt[2] = amt[2] - maxMilk[0]
            print(amt[0])
    
    pourNum += 1

print("answer: ", amt[0], amt[1], amt[2])