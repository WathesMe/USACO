#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=917
#Solution Link: https://usaco.guide/problems/usaco-917-measuring-traffic/solution
#Score: 10/10 - 100%

list1 = list()
tbd1 = 0
tbd2 = 10 ** 18

with open("traffic.in") as read:
    N = int(read.readline())
    list1 = list()
    for _ in range(N):
        c, a, b = read.readline().split()
        a = int(a)
        b = int(b)
        list1.append((c, a, b))

for i in range(N):
    if list1[i][0] == "none":
        tbd1 = max(tbd1, list1[i][1])
        tbd2 = min(tbd2, list1[i][2])
    if list1[i][0] == "on":
        tbd1 += list1[i][1]
        tbd2 += list1[i][2]
    if list1[i][0] == "off":
        tbd1 -= list1[i][2]
        tbd2 -= list1[i][1]

tbd1 = max(tbd1, 0)

tbd3 = tbd1
tbd4 = tbd2

for i in reversed(range(N)):
    if list1[i][0] == "none":
        tbd3 = max(tbd3, list1[i][1])
        tbd4 = min(tbd4, list1[i][2])
    if list1[i][0] == "on":
        tbd3 -= list1[i][2]
        tbd4 -= list1[i][1]
    if list1[i][0] == "off":
        tbd3 += list1[i][1]
        tbd4 += list1[i][2]

with open("traffic.out", "w") as written:
    print(max(tbd3, 0), tbd4, file=written)
    print(max(tbd1, 0), tbd2, file=written)