import sys
# use print to sys.stderr for debug, e.g.
# print(values[current], file=sys.stderr)

def solve(b):
    values = [-1] * b
    current = 0
    verifyIndex = [0, -1]
    verifyValues = [-1, -1]
    to_verify = False

    for r in range(15):
        for i in range(10):
            paired = b - current - 1
            if to_verify and (i == 0 or i == 1):
                if verifyIndex[i] == -1:
                    print("1")
                else:
                    print(verifyIndex[i] + 1)
                sys.stdout.flush()
                verifyValues[i] = int(input())

                if i == 1:
                    to_verify= False
                    # verify one value
                    if verifyIndex[1] == -1: # i.e i = 0
                        if values[verifyIndex[0]] != verifyValues[0]: # otherwise treat as same
                            # assume flip because it's always correct
                            for j in range(0, b):
                                values[j] = 1 - values[j]
                        continue
                    # verify two values
                    # verifyIndex[0] and verifyIndex[1]
                    # 0,0 => 0 and 0,1 => 0: same
                    # 0,0 => 0 and 0,1 => 1: reverse
                    # 1,1 => 0 and 0,1 => 0: reverse flipped
                    # 1,1 => 0 and 0,1 => 1: flipped
                    # 0,0 => 0 and 1,0 => 0: reverse
                    # 0,0 => 0 and 1,0 => 1: same
                    # 1,1 => 0 and 1,0 => 0: flipped
                    # 1,1 => 0 and 1,0 => 1: reverse flipped
                    if verifyValues[0] == values[verifyIndex[0]] and verifyValues[1] == values[verifyIndex[1]]:
                        # same
                        pass
                    elif verifyValues[0] != values[verifyIndex[0]] and verifyValues[1] != values[verifyIndex[1]]:
                        #flipped
                        for j in range(0, b):
                            values[j] = 1 - values[j]
                    elif verifyValues[0] == values[verifyIndex[0]] and verifyValues[1] != values[verifyIndex[1]]:
                        # reverse
                        values.reverse()
                    elif verifyValues[0] != values[verifyIndex[0]] and verifyValues[1] == values[verifyIndex[1]]:
                        # reverse flipped
                        values.reverse()
                        for j in range(0, b):
                            values[j] = 1 - values[j]
            else:
                print(current + 1)
                sys.stdout.flush()
                values[current] = int(input())

                if current >= int(b / 2) and verifyIndex[1] == -1 and current != b - 1:
                    # check if can use as second verifying
                    if (values[0] + values[b - 1] + values[paired] + values[current]) % 2 == 1:
                        # use 0 as same pair; 1 as different pair
                        if values[0] != values[b - 1]:
                            verifyIndex[1] = verifyIndex[0]
                            verifyIndex[0] = paired
                        else:
                            verifyIndex[1] = paired # or current

                if paired < current:
                    if paired + 1 >= current:
                        # finished
                        print("".join([str(x) for x in values]))
                        response = input()
                        if response == "N":
                            sys.exit()
                        return
                    current = paired + 1
                else:
                    current = paired

            if i == 9:
                to_verify = True


t = [t, b] = [int(x) for x in input().split(" ")]
for _ in range(t):
    solve(b)
sys.exit()
