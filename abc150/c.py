import itertools

a = int(input())
b = input().split()
c = input().split()

def x(z):
    return sorted(list(itertools.permutations(z))).index(tuple(z)) + 1

print(abs(x(b) - x(c)))