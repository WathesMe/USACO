def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def main():
    N, K = map(int, input().split())
    Q = int(input())

    M = N - K + 1

    A = [[0] * (N + 1) for _ in range(N + 1)]
    S = [[0] * (M + 1) for _ in range(M + 1)]

    best = 0

    for _ in range(Q):
        r, c, newv = map(int, input().split())

        oldv = A[r][c]
        delta = newv - oldv
        A[r][c] = newv

        i1 = max(1, r - K + 1)
        i2 = min(M, r)
        j1 = max(1, c - K + 1)
        j2 = min(M, c)

        for i in range(i1, i2 + 1):
            rowS = S[i]
            for j in range(j1, j2 + 1):
                val = rowS[j] + delta
                rowS[j] = val
                if val > best:
                    best = val

        print(best)


if __name__ == "__main__":
    main()
