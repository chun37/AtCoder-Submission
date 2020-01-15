a = input()
b = input()
index = 0
find = "ABC"
count = 0

while index < int(a):
    i = b[index:].find(find)
    if i == -1:
        break
    index += i + 3
    count += 1

print(count)