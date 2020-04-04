from bisect import bisect

k = int(input())
A = list(range(10))

if k <= 9:
    print(A[k])
    exit()


def is_1_keta(i):
    return len(str(i)) == 1


kouho = list(map(str, range(1, 10)))
kouho2 = list(map(str, range(1, 10)))
while True:
    ll = []
    for i in kouho:
        su = list(filter(is_1_keta, [int(i[-1]) - 1, int(i[-1]), int(i[-1]) + 1]))
        l = [str(i) + str(x) for x in su]
        A.extend(l)
        ll.extend(l)
    kouho = ll
    kouho2.extend(ll)
    if len(kouho2) > k:
        break

print(sorted(list(map(int, kouho2)))[k - 1])
