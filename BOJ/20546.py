def jh():
    stock, cash = 0, money
    for price in prices:

        if price <= cash:
            stock += (cash // price)
            cash %= price

    return cash + stock * prices[-1]


def sm():
    stock, cash = 0, money
    check = 0
    for i, price in enumerate(prices[1:]):
        if price > prices[i]:  # 가격 하락
            if check < 0:
                check -= 1
            else:
                check = -1
        elif price < prices[i]:  # 가격 상승
            if check > 0:
                check += 1
            else:
                check = 1
        if check >= 3 and price <= cash:
            stock += (cash // price)
            cash %= price
        elif check <= -3:
            cash += (price * stock)
            stock = 0

    return cash + stock * prices[-1]


money = int(input())
prices = list(map(int, input().split()))

JH, SM = jh(), sm()
if JH > SM:
    print("BNP")
elif JH < SM:
    print("TIMING")
else:
    print("SAMESAME")
