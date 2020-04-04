n, m = input().split()
l = sorted(list(map(int, input().split())))
sum_touhyou = sum(l)
line_touhyou = sum_touhyou * (1 / (int(m) * 4))

r = [i for i in l if i >= line_touhyou]

if len(r) >= int(m):
    print("Yes")
else:
    print("No")
