N, M = map(int, input().split())
A = list(map(int, input().split()))
if (res := N - sum(A)) < 0:
    print(-1)
else:
    print(res)
