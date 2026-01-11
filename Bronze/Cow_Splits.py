T, K = map(int, input().split())
N = list()
S = list()
ans = -1
allowed = ["CO", "OW", "WC"]

def find_pair_indices(block, pair):
    a, b = pair[0], pair[1]
    for i in range(3):
        if block[i] != a:
            continue
        for j in range(i + 1, 3):
            if block[j] == b:
                return i, j
    return None

for _ in range(T):
    a = int(input())
    b = input()
    N.append(a)
    S.append(b)

for i in range(T):
    n = N[i]
    s = S[i]
    L = len(s)
    midpoint = L // 2

    part1 = s[:midpoint]
    part2 = s[midpoint:]

    if n % 2 == 1 or L != 3 * n:
        ans = -1
    elif part1 == part2:
        list1 = [1] * L
        ans = 1
    else:
        ans = 2
        list1 = [0] * L
        chunks1 = [part1[x:x+3] for x in range(0, len(part1), 3)]
        chunks2 = [part2[x:x+3] for x in range(0, len(part2), 3)]

        ok = True
        for j, (c1, c2) in enumerate(zip(chunks1, chunks2)):
            chosen = None
            for p in allowed:
                p1 = find_pair_indices(c1, p)
                if p1 is None:
                    continue
                p2 = find_pair_indices(c2, p)
                if p2 is None:
                    continue
                chosen = (p1, p2)
                break

            if chosen is None:
                ok = False
                break

            (a1, b1), (a2, b2) = chosen
            base1 = j * 3
            base2 = midpoint + j * 3

            list1[base1 + a1] = 1
            list1[base1 + b1] = 1
            for t in range(3):
                if t != a1 and t != b1:
                    list1[base1 + t] = 2

            list1[base2 + a2] = 1
            list1[base2 + b2] = 1
            for t in range(3):
                if t != a2 and t != b2:
                    list1[base2 + t] = 2

        if not ok:
            ans = -1

    print(ans)
    if ans != -1:
        print(*list1)
        # print("hello")
    list1 = list()
