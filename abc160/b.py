coins = [500, 5, 100, 50, 10, 1]
uresimi = {500: 1000, 5: 5}


def get_uresimi(money, coin_type):
    coin_count = money // coin_type
    if coin_count == 0:
        return 0, money
    surplus = money % (coin_type * coin_count)
    uresisa = uresimi.get(coin_type, 0) * coin_count
    return uresisa, surplus


m = int(input())
uresii = 0
for c in coins:
    u, m = get_uresimi(m, c)
    uresii += u

print(uresii)
