list1 = list(map(int, input().split()))
M = list1[0] #Vertical Size
N = list1[1] #Horizontal Size
K = list1[2] #Scale Factor
signal = list() #Signal Input
grid = list()
grid2 = list()

#arr = [[0]*N for _ in range(M)] #2D Array

for j in range(M):
    grid.append(list(input().strip()))
    print(grid)

print(grid)

arr2 = [[0]*(N*K) for _ in range(M*K)] #Scaled 2D Array

for k in range(M):
    grid2.copy(arr2)