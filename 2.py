def ans(s):
    current = 0
    ans = ""
    for i in range(0, len(s)):
        if s[i] > current:
            ans += "(" * (s[i] - current)
        elif s[i] < current:
            ans += ")" * (current - s[i])
        ans += str(s[i])
        current = s[i]
    if current > 0:
        ans += ")" * current
    return ans


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    s = list(map(int, list(input())))
    print("Case #{}: {}".format(i, ans(s)))
