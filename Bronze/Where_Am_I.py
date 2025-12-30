#USACO EASY PROBLEM 2 - WHERE AM I?
N = int(input())
string = str(input())
ans = 0

K = 0
count = 0

for j in range(len(string) - N + 1):
    if ans == string:
        break
    for i in range(len(string) - N + 1):
        substring = string[i : i + N]
        splitt = string.split(substring)
        if len(splitt) > 2:
            N += 1
            ans = N
            break

print(ans)