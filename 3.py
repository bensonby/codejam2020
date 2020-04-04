def ans(s):
    c = -1
    j = -1
    ans = []
    length = len(s)
    sort_values = [[x[0], x[1], x[0] * 1440 + x[1] + i / 1500.0, i] for i, x in enumerate(s)]
    s2 = sorted(sort_values, key = lambda x: x[2])
    key2 = sorted(range(length), key = lambda x: s2[x][3])
    for i in range(length):
        if s2[i][0] >= c:
            ans.append("C")
            c = s2[i][1]
        elif s2[i][0] >= j:
            ans.append("J")
            j = s2[i][1]
        else:
            return "IMPOSSIBLE"
    return "".join(list(map(lambda x: ans[key2[x]], range(length))))


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    s = list(map(lambda x: list(map(int, input().split(" "))), range(n)))
    print("Case #{}: {}".format(i, ans(s)))
