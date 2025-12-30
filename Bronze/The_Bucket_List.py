N = int(input()) #Number of cows

start = list() #Starting time
end = list() #Ending time
buckets = list() #Number of buckets needed per cow

total = 0
ans = 0 #Literally number of buckets needed total

tbe = list()

for _ in range(N):
    s, e, b = map(int, input().split())
    tbe.append((s, b))
    tbe.append((e, -b))

tbe.sort()
for i in range(N*2):
    total = total + tbe[i][1]

    if total > ans:
        ans = total

print(ans)