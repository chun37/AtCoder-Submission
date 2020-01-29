N = int(input())
p = [int(i) for i in input().split()]
p = [0] + p

cc = 0
i_list = list(range(1, N + 1))
for i in i_list:
    j_list = [x for x in range(1, i + 1)]
    print(j_list)
    for j in j_list:
        print(j)
        if p[i] <= p[j]:
            cc += 1
            print("add")
            break


print(cc)