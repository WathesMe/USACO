#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=891
#Solution Link: https://usaco.guide/bronze/simulation?lang=py

N = int(input()) #swaps
list1 = []

pebble = 1 #The position pebble is in

count = 0 #Number of times the correct variable was guessed
countMax = 0 #Answer

for _ in range(N): #Getting the lines and stuff into a list
    line = input()
    list1.append(line) #Adding lines into list


    #listt.append(a, b, g)

for i in range(N):
    pebble = i + 1
    count = 0
    for j in range(N): #Setting each line of input as 3 variables. Number 1 is a, 2 is b, 3 is g
        
        a, b, g = list1[j].split()
            
        a = int(a)
        b = int(b)
        g = int(g)

        if pebble == a: #swapping pebble pos
            pebble = b
        elif pebble == b:
            pebble = a
        
        if pebble == g: #if guessed right, add 1 to count
            count += 1

    if count > countMax: #Find largest count
        countMax = count
        
 

print(countMax) #Print answer