# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import permutations


def solution(S):
    # write your code in Python 3.6
    # print(S.split(':'))
    # print(list(S))
    ind = list(S.split(':'))
    # print(ind[1])
    if (int(ind[1][::-1])) > int(ind[1]) and (int(ind[1][::-1])) < 60:
        res = ind[0] + ":" + ind[1][::-1]
        # print(res)
        return res
    x = list(S)
    # print(x)
    iterated = 0

    for item in x:
        iterated += 1
        if item is ':':
            x.remove(item)
    # print(x)
    perms = [''.join(p) for p in permutations(x, 2)]
    # print(perms)
    prev = int(ind[0])
    k = []
    for item in perms:
        if int(item) < 24 and (int(item) > int(ind[0]) or int(item) is 0):

            if len(k) == 0:
                k.append(item)
            else:
                if int(item) < int(k[0]):
                    k[0] = item

    if len(k) == 0:
        k.append(ind[0])
    # print(list(k[0]))
    # print("---")
    hor = (''.join(list(k[0])))
    shr = list(k[0])
    iterated = 1
    for item in shr:
        iterated = 1
        for _it in x:
            if _it is item and iterated is 1:
                x.remove(item)
                iterated = 0
    # print(''.join(x))
    minperms = [''.join(p) for p in permutations(x, 2)]
    # min = (''.join(x))
    # if int(min[::-1]) <
    # print(minperms)
    if int(minperms[0]) < int(minperms[1]):
        min = minperms[0]
    else:
        min = minperms[1]
    # print(hor)
    # print(min)
    result = hor + ":" + min
    return result

    pass