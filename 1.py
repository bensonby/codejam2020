def check_numbers(n, numbers):
    filled = list(map(lambda x: 1, range(n)))
    for i in range(0, n):
        if numbers[i] <= 0 or numbers[i] > n:
            return False
        filled[numbers[i] - 1] = 0
    return sum(filled) == 0


def row(n, v):
    incorrect = 0

    for i in range(0, n):
        incorrect += 0 if check_numbers(n, v[i]) else 1
    return incorrect


def column(n, v):
    incorrect = 0

    for i in range(0, n):
        incorrect += 0 if check_numbers(n, list(map(lambda x: v[x][i], range(n)))) else 1
    return incorrect


def trace(n, v):
    trace = sum(list(map(lambda x: v[x][x], range(0, n))))
    return trace


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    v = []
    for j in range(1, n + 1):
        v.append(list(map(int, input().split(" "))))
    print("Case #{}: {} {} {}".format(i, trace(n, v), row(n, v), column(n, v)))
