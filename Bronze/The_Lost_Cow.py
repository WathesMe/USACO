#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=735
#Solution Link: https://usaco.guide/bronze/simulation?lang=py

list1 = input() #[0] is Farmer pos, [1] is Cow pos
farmerPos, cowPos = list1.split()
farmerPos = int(farmerPos)
cowPos = int(cowPos)
farmerOG = farmerPos

smaller = True
move = 1
total = 0
newFarmerPos = 0

if farmerPos > cowPos:
    smaller = False

while True:
    total = total + abs(move) + abs(farmerPos - farmerOG)

    farmerPos = farmerOG + move
    print(farmerPos)
    move = move*-2
    
    #print(move)
    
    if smaller == True and farmerPos >= cowPos:
        total = total - (farmerPos - cowPos)
        print(total)
        break
    if smaller == False and farmerPos <= cowPos:
        total = total - (abs(cowPos - farmerPos))
        print(total)
        break