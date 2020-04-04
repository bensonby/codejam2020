import sys

def solve(b):
    values = []
    values.append([-1] * b)

    # print(n, file=sys.stderr)
    for _ in range(15):
        for i in range(10):
            current = 1
            print(current)
            sys.stdout.flush()
            v = int(input())
        if prefs[0] == -1:
            sys.exit()
        d = prefs.pop(0)
        # print("--1", file=sys.stderr)
        if d == 0:
            print('-1')
            sys.stdout.flush()
            continue
        # print("--2", file=sys.stderr)
        for flavor in prefs:
            counts[flavor] = counts[flavor] + 1

        # print("--3", file=sys.stderr)
        relevant_counts = [counts[flavor] for flavor in prefs]
        min_flavor_id = 0
        for i in range(1, d):
            if relevant_counts[i] < relevant_counts[min_flavor_id]:
                min_flavor_id = i
        # print("--4", file=sys.stderr)
        min_flavor = prefs[min_flavor_id]
        if counts[min_flavor] > 10000:
            print('-1')
            sys.stdout.flush()
            continue
        # print("--5", file=sys.stderr)
        # sell flavor id min_flavor
        counts[min_flavor] = 10001
        print(min_flavor)
        sys.stdout.flush()


t = int(input())
b = int(input())
# print(t, file=sys.stderr)
for _ in range(t):
    # print("--------------", file=sys.stderr)
    # n = int(input())
    # result = solve(n)
    solve(b)
    # if result == -1:
sys.exit()
