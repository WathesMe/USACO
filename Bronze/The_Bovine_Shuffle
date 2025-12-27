#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=760
#Solution Link: https://usaco.guide/problems/usaco-760-the-bovine-shuffle/solution

N = int(input()) #Number of Cows
order = list(map(int, input().split())) #Order of cows
ids = list(map(int, input().split())) #Ids of cows
ans = list(range(N)) #Answer list

for i in range(N):
    ans[order[i] - 1] = ids[i]

for j in range(N):
    print(ans[j])