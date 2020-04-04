def ans(s):
    c = -1
    j = -1
    ans = []
    s2 = sorted(s, key = lambda x: x[0])
    key2 = sorted(range(len(s)), key = lambda x: s[x][0])
    for i in range(len(s2)):
        if s2[i][0] >= c:
            ans.append("C")
            c = s2[i][1]
        elif s2[i][0] >= j:
            ans.append("J")
            j = s2[i][1]
        else:
            return "IMPOSSIBLE"
    return "".join(list(map(lambda x: ans[key2[x]], range(len(s)))))


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    s = list(map(lambda x: list(map(int, input().split(" "))), range(n)))
    print("Case #{}: {}".format(i, ans(s)))
