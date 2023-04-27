# An improved version of the solution to foobar level 3 task 1
# The solution I handed in is called solution_orig() but the day after I handed it in a better solution (more vectorized)

import numpy as np

np.seterr(divide='ignore', invalid='ignore')


def solution(l):
    length = len(l)
    tril = np.tril(np.ones((length, length)), -1)
    divisors = (np.array(l).reshape((length, 1)))
    return int(np.sum(((np.mod(divisors, tril * l) == 0).astype(int)) * np.sum((np.mod(divisors, tril * l) == 0).astype(int), axis=1)))


def solution_orig(l):
    length = len(l)
    triple_count = 0
    divisors = np.zeros(length)

    for i in range(0, length):
        temp = (np.mod(l[i], l[:i]) == 0).astype(int)
        divisors[i] = np.sum(temp)
        temp = np.append(temp, [0] * (length - i))
        triple_count += np.sum(temp * divisors)

    return triple_count