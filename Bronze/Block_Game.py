#Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=664
#Solution Link: https://usaco.guide/problems/usaco-664-block-game/solution
#Score: 10/10 - 100%

from collections import Counter

with open("blocks.in") as read:
	N = int(read.readline())
	pairs = [read.readline().split() for _ in range(N)]

# Build line_dicts: a list of (dict_for_w1, dict_for_w2)
line_dicts = []
for w1, w2 in pairs:
    d1 = dict(Counter(ch for ch in w1.lower() if 'a' <= ch <= 'z'))
    d2 = dict(Counter(ch for ch in w2.lower() if 'a' <= ch <= 'z'))
    for k, v in d2.items():       # loop d2 (line 17 in your file)
        if k in d1:
            if v > d1[k]:
                d1[k] = v    # keep the bigger value
        else:
            d1[k] = v        # add new key from d2
    print(d1)
    line_dicts.append(d1)

# Merge all dictionaries in line_dicts, summing values for shared keys
merged = Counter()
for d in line_dicts:
    merged.update(d)

list1 = [0] * 26
for k, v in merged.items():
    position = ord(k) - ord('a')
    list1[position] = v

with open("blocks.out", "w") as written:
	for i in list1:
		print(i, file=written)