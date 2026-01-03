#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=831
#Solution Link: https://usaco.guide/problems/usaco-831-team-tic-tac-toe/solution
#Score: 10/10 - 100%

jeff = list()
list2 = list()
list1 = list()
solo = set()
group = set()

with open("tttt.in") as read:
    for _ in range(3):
        list2.append(read.readline().strip())

list1.append(tuple(list2[0]))
list1.append(tuple(list2[1]))
list1.append(tuple(list2[2]))

for i in range(3): #Adding stuff to lists
    jeff.append(set((list1[i][0], list1[i][1], list1[i][2])))
    jeff.append(set((list1[0][i], list1[1][i], list1[2][i])))

jeff.append(set((list1[0][0], list1[1][1], list1[2][2])))
jeff.append(set((list1[0][2], list1[1][1], list1[2][0])))

print(jeff)
for i in range(len(jeff)): #Group
    if len(jeff[i]) == 1:
        bob = list(jeff[i])
        john = bob[0]
        solo.add(john)
    if len(jeff[i]) == 2:
        joe = tuple(sorted(jeff[i]))
        group.add(joe)

with open("tttt.out", "w") as written:   
    print(len(solo), file=written)
    print(len(group), file=written)