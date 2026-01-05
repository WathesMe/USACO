#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=615
#Solution Link: https://usaco.guide/problems/usaco-615-milk-pails/solution
#Score: 10/10 - 100%

with open("pails.in") as read:
    X, Y, M = map(int, read.readline().split())
a = int(M//X)
b = int(M//Y)
list1 = list()
ans = 10**18

for i in range(a + 1):
    for j in range(b + 1):
        bob = M - (X*i + Y*j)
        list1.append(bob)

for i in range(len(list1)):
    if list1[i] >= 0:
        ans = min(list1[i], ans)

with open("pails.out", "w") as written:
    print(M - ans, file=written)