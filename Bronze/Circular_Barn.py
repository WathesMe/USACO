#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=616
#Solution Link: https://usaco.guide/problems/usaco-616-circular-barn/solution
#Score: 10/10 - 100%

with open("cbarn.in") as read:
    N = int(read.readline())
    list1 = list()
    for _ in range(N):
        list1.append(int(read.readline().strip()))

mult = 0
bob = 0
ans = 10**18
lost = 0

for i in range(N):
    for j in range(N):
        bob = bob + (list1[j] * mult)
        mult += 1

    ans = min(bob, ans)
    mult = 0
    bob = 0

    lost = list1.pop(0)
    list1.append(lost)

with open("cbarn.out", "w") as written:
    print(ans, file=written)