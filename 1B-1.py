def solve(x, y):
    if x % 2 + y % 2 != 1:
        return "IMPOSSIBLE"
    if x % 2 == 1:
        if x == 1 and y == 0:
            return "E"
        if x == -1 and y == 0:
            return "W"
        new_y = int(y / 2)
        if ((x - 1) / 2) % 2 + new_y % 2 == 1:
            return "E" + solve(int((x - 1) / 2), new_y)
        else:
            return "W" + solve(int((x + 1) / 2), new_y)
    else:
        if y == 1 and x == 0:
            return "N"
        if y == -1 and x == 0:
            return "S"
        new_x = int(x / 2)
        if ((y - 1) / 2) % 2 + new_x % 2 == 1:
            return "N" + solve(new_x, int((y - 1) / 2))
        else:
            return "S" + solve(new_x, int((y + 1) / 2))


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    x, y = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, solve(x, y)))

