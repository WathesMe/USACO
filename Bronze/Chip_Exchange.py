import sys

INF = 10**18

def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b

def worst_final_A(A: int, B: int, cA: int, cB: int, x: int) -> int:
    k_top = (B + x) // cB
    best = A + k_top * cA

    k_low = ceil_div(B + 1, cB) - 1
    k_high = (B + x + 1) // cB - 1

    if k_low <= k_high:
        k = k_low if cA >= cB else k_high
        val = A + x + B + 1 - cB + k * (cA - cB)
        best = min(best, val)

    return best

def findAns(A: int, B: int, cA: int, cB: int, fA: int) -> int:
    if A >= fA:
        return 0

    lo, hi = 0, INF
    while lo < hi:
        mid = (lo + hi) // 2
        if worst_final_A(A, B, cA, cB, mid) >= fA:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    T = int(data[0])
    idx = 1

    ans = []
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx + 1])
        cA = int(data[idx + 2])
        cB = int(data[idx + 3])
        fA = int(data[idx + 4])
        idx += 5

        ans.append(str(findAns(A, B, cA, cB, fA)))

    for i in range(T):
        print(ans[i])

main()