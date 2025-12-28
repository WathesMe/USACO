#Question Link: https://usaco.org/index.php?page=viewproblem2&cpid=665
#Solution Link: https://usaco.guide/problems/usaco-665-the-cow-signal/solution

list1 = list(map(int, input().split()))
M = list1[0] #Vertical Size
N = list1[1] #Horizontal Size
K = list1[2] #Scale Factor
signal = list() #Signal Input
grid = list()
grid2 = list()

for j in range(M):
    grid.append(list(input().strip()))

arr2 = [[0]*(N*K) for _ in range(M*K)] #Scaled 2D Array

for i in range(M):
    for j in range(N):
        for k in range(K):
            for l in range(K):
                arr2[K*i + k][K*j + l] = grid[i][j]

for i in range(M*K):
    print(*arr2[i])