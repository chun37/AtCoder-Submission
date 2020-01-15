text = input()

k, x = map(int, text.split())
if 500 * k >= x:
    print("Yes")
else:
    print("No")