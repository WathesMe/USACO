#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=1491
#Solution Link (External): https://usaco.org/current/data/sol_prob1_bronze_feb25.html
#Score: 16/16 - 100% 

N, U = map(int, input().split())
list1 = list()
grid = list()
bob = list()
r = list()
c = list()
jeff = 1
ans = list()

for _ in range(N):
    list1.append(input().strip())

for _ in range(U):
    a, b = map(int, input().split())
    r.append(a)
    c.append(b)

for i in range(N):
    grid.append(list(list1[i]))

swaps = 0
count = [[0] * int(N/2) for _ in range(int(N/2))]
for i in range(int(N/2)):
    for j in range(int(N/2)):
        p1 = grid[i][j]
        p2 = grid[i][N - 1 - j]
        p3 = grid[N - 1 - i][j]
        p4 = grid[N - 1 - i][N - 1 - j]
        
        score = [p1, p2, p3, p4].count('#')
        count[i][j] = score
        swaps += min(score, 4 - score)

ans.append(swaps)
for i in range(U):
    newR = r[i] - 1
    newC = c[i] - 1

    if newR < int(N/2):
        j = newR
    else:
        j = (N - 1) - newR

    if newC < int(N/2):
        k = newC
    else:
        k = (N - 1) - newC
    
    old_score = count[j][k]
    swaps -= min(old_score, 4 - old_score)

    if grid[newR][newC] == '#':
        grid[newR][newC] = '.'
        count[j][k] -= 1
    else:
        grid[newR][newC] = '#'
        count[j][k] += 1

    new_score = count[j][k]
    swaps += min(new_score, 4 - new_score)
    
    ans.append(swaps)

for i in range(U + 1):
    print(ans[i])