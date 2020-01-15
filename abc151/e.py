import itertools

n, k = map(int, input().split())
all_list = [int(i) for i in input().split()]


def f(combi):
    return max(combi) - min(combi)

res = sum(map(f, itertools.combinations(all_list, k)))

print(divmod(res,  10 ** 9 + 7)[1])