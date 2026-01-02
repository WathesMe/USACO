#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=593
#Solution Link: https://usaco.guide/problems/usaco-593-mowing-the-field/solution
#Score: 10/10 - 100%

directions = list() #after 4 datastructure changes i have decided on list
t = 0
x, y = 0, 0 #Coordinates. ok this is com;licaterd :(
dict1 = dict()
ans = 10**10

with open("mowing.in") as read:
    N = int(read.readline())
    for _ in range(N): #Put stuff in list
        a, b = read.readline().split()
        b = int(b)
        directions.append((a, b))

for i, j in directions:
    for k in range(j):
        if i == "N": #North
            t += 1
            y += 1
        if i == "E": #East
            t += 1
            x += 1
        if i == "S": #South
            t += 1
            y -= 1
        if i == "W": #West
            t += 1
            x -= 1
        if (x, y) in dict1.keys(): #Check if we have been here before
            ans = min(t - dict1[(x, y)], ans) #If yes, find difference in time
        dict1.update({(x, y) : t})
if ans == 10**10:
    ans = min(-1, ans)

with open("mowing.out", "w") as written:
    print(ans, file=written)