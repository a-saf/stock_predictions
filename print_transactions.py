import numpy as np
import math


# main function that prints the transactions
def printTransactions(m, k, d, name, owned, prices):
    money_available = m
    transactions = []

    for i in range(k):
        stock_count = 0
        sum_xy = 0
        stock_prices = []

        sum_days = sum(range(1, days[name[i]]+1))

        with open(name[i] + ".txt") as file:
            for line in file:
                line = line.strip()
                stock_prices.append(float(line))

        prices_len = len(stock_prices)

        sum_x = sum(stock_prices)
        sqr_stock_prices = list(np.array(stock_prices) ** 2)
        sum_sqr_x = sum(sqr_stock_prices)

        for j in range(prices_len):
            sum_xy += stock_prices[j] * (days[name[i]]-j)
        # calculate slope for each stock using slope formula for linear regression
        slope = (sum_xy - sum_days * sum_x / prices_len) / (sum_sqr_x - (sum_x ** 2)/prices_len)

        # sell all stocks with decreasing prices
        if slope < 0 and owned[i] > 0:
            transactions.append(name[i] + " SELL " + str(owned[i]))
            owned[i] = 0
        # buy stocks that show an increasing trend in prices
        elif slope > 0:
            while money_available >= stock_prices[prices_len-1]:
                money_available -= stock_prices[prices_len-1]
                owned[i] += 1
                stock_count += 1
            if stock_count > 0:
                transactions.append(name[i] + " BUY " + str(stock_count))

        # do nothing for stocks that show no price change?

    # print transactions to stdout
    if len(transactions) > 0:
        print(len(transactions))
        for x in range(len(transactions)):
            print(transactions[x])
    else:
        print(0)


# get and sanitize input
line_one = input()
list_one = line_one.split(" ", 2)
m = float(list_one[0])
k = int(list_one[1])
d = int(list_one[2])
name = []
owned = []
prices = []

days = {}

for p in range(k):
    stock_info = input()
    stock_list = stock_info.split(" ", 6)
    name.append(stock_list[0])
    owned.append(int(stock_list[1]))
    prices.append(float(p) for p in stock_list[2:7])

    f = open(stock_list[0] + ".txt", "a+")
    for q in range(2, 7):
        f.write(stock_list[q] + "\n")
    f.close()

    if stock_list[0] not in days:
        days[stock_list[0]] = 0
    days[stock_list[0]] = days[stock_list[0]] + 5

printTransactions(m, k, d, name, owned, prices)
