a, b = input().split()

x = a * int(b)
y = b * int(a)

print(sorted([x, y])[0])
