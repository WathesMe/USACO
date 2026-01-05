#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=639\
#Solution Link: https://usaco.guide/problems/usaco-639-diamond-collector/solution
#Score: 10/10 - 100%

sizes = list()
with open("diamond.in") as read:
    N, K = map(int, read.readline().split())
    for _ in range(N):
        sizes.append(int(read.readline()))
ans = 0
count = 0

sizes = sorted(sizes)
for i in range(N):
    bob = sizes[i] + K
    for j in range(N):
        if sizes[j] <= bob and sizes[j] >= sizes[i]:
            count += 1
    ans = max(ans, count)
    count = 0

with open("diamond.out", "w") as written:
    print(ans, file=written)