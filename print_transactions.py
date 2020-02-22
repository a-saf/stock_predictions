import numpy as np
import math


# main function that prints the transactions
def printTransactions(m, k, d, name, owned, prices):
    money_available = m
    transactions = []
    days = [5, 4, 3, 2, 1]

    for i in range(k):
        stock_count = 0
        sum_xy = 0

        stock_prices = list(prices[i])
        sum_x = sum(stock_prices)
        sqr_stock_prices = list(np.array(stock_prices) ** 2)
        sum_sqr_x = sum(sqr_stock_prices)

        for j in range(5):
            sum_xy += stock_prices[j] * days[j]
        # calculate slope for each stock using slope formula for linear regression
        # sum of days is 15
        slope = (5 * sum_xy - 15 * sum_x) / (5 * sum_sqr_x - sum_x ** 2)

        # sell all stocks with decreasing prices
        if slope < 0 and owned[i] > 0:
            transactions.append(name[i] + " SELL " + str(owned[i]))
            owned[i] = 0
        # buy stocks that show an increasing trend in prices
        elif slope > 0:
            while money_available >= stock_prices[4]:
                money_available -= stock_prices[4]
                owned[i] += 1
                stock_count += 1
            if stock_count > 0:
                transactions.append(name[i] + " BUY " + str(stock_count))

    # do nothing for stocks that show no price change?

    # print transactions to stdout
    if len(transactions) > 0:
        print(len(transactions))
        for m in range(len(transactions)):
            print(transactions[m])
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

for i in range(k):
    stock_info = input()
    stock_list = stock_info.split(" ", 6)
    name.append(stock_list[0])
    owned.append(int(stock_list[1]))
    prices.append(float(i) for i in stock_list[2:7])

printTransactions(m, k, d, name, owned, prices)
