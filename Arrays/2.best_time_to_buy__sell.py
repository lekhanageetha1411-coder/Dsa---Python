prices = [7,1,2,3,4,6,5]

min_price = prices[0]
max+profit = 0

for p in prices:
    if p < min_profit:
        min_price = p

        profit = p - min_price

    if profit > max_profit:
        max_profit = profit
print(max_profit)