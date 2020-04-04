n, k = map(int, input().split())

r = []
n = n % k
if n == 0:
    print(0)
    exit()
while True:
    n = abs(n - k)
    r.append(n)
    if r.count(n) >= 2:
        break

print(min(r))
