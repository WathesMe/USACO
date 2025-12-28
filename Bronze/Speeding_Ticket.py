n, m = list(map(int, input().split())) #N = Road M = Cow
road = list()
cow = list()
total = 0
ans = 0

for _ in range(n):
    road.append(list(map(int, input().split())))

for _ in range(m):
    cow.append(list(map(int, input().split())))

i, j = 0, 0
while True:
    total = cow[i][1] - road[j][1]

    if cow[i][0] - road[j][0] == 0: #Move both to next bracket
        i += 1
        j += 1
    elif cow[i][0] - road[j][0] > 0: #Move only Road to next bracket
        cow[i][0] = abs(cow[i][0] - road[j][0])
        j += 1
    elif cow[i][0] - road[j][0] < 0: #Move only Cow to next bracket
        road[j][0] = abs(cow[i][0] - road[j][0])
        i += 1

    if total > ans:
        ans = total
    
    if i == m or j == n:
        break

print(ans)