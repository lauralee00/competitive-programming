import sys
import math
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(read())
        cnta = defaultdict(list)
        for i, elem in enumerate(a):
            cnta[elem].append(i)
        if n == 1 or len(cnta) == 1:
            print(0)
            continue
        elif len(cnta) == 2 and len(cnta[1]) > 0:
            for elem in cnta:
                if elem != 1:
                    if len(cnta[elem]) % 2 != 0: # invalid
                        print(-1)
                        break
                    else:
                        print(len(cnta[elem]))
                        for i in range(0, len(cnta[elem]), 2):
                            print(cnta[elem][i], cnta[elem][i+1])

            continue
        else:
            min_num = min(a)
            ops = []
            ones = True
            while len(ops) <= 33*n and len(cnta) > 1:
                for elem1 in cnta:
                    if elem1 == 1:

                        del cnta[1]
                        break
                    for elem2 in cnta:
                        if elem2 == 1:

                            del cnta[1]
                            break
                        if elem1 != elem2:
                            if elem1 > elem2:
                                tmp = math.ceil(elem1/elem2)
                                for idx in cnta[elem1]:
                                    ops.append((idx, cnta[elem2][0]))
                                for idx in cnta[elem2]:
                                    ops.append((idx, cnta[elem1][0]))

                                tmp2 = math.ceil(elem2/tmp)
                                if tmp > 1:
                                    cnta[tmp].extend(list(cnta[elem1]))


                                if tmp2 > 1:
                                    cnta[math.ceil(elem2/tmp)].extend(list(cnta[elem2]))


                                del cnta[elem1]
                                del cnta[elem2]

                            else:
                                tmp = math.ceil(elem2/elem1)
                                for idx in cnta[elem1]:
                                    ops.append((idx, cnta[elem1][0]))
                                for idx in cnta[elem2]:
                                    ops.append((idx, cnta[elem2][0]))
                                if tmp > 1:
                                    cnta[tmp].extend(cnta[elem2])

                                tmp2 = math.ceil(elem1/tmp)
                                cnta[math.ceil(elem1/tmp)].extend(list(cnta[elem1]))
                                if tmp2 > 1:
                                    cnta[math.ceil(elem1/tmp)].extend(list(cnta[elem1]))

                                del cnta[elem1]
                                del cnta[elem2]
                        else:
                            continue
                        break
                    break
            if len(cnta) != 1:
                print(-1)
                continue

            if ones:
                tmp = None
                for elem in cnta:
                    tmp = elem
                    break

                if len(cnta[tmp]) % 2 != 0:
                    print(-1)
                    continue
                else:
                    for i in range(len(cnta[tmp])):
                        for j in range(i+1, len(cnta[tmp])):
                            ops.append((i, j))

            print(len(ops))
            for a, b in ops:
                print(a + 1, b + 1)


            continue



if __name__ == '__main__':
    solve()
