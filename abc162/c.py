import itertools
import math

K = int(input())


def _gcd(a, b, c):
    return math.gcd(c, math.gcd(a, b))


print(sum(map(lambda x: _gcd(*x), itertools.product(range(1, K + 1), repeat=3))))
