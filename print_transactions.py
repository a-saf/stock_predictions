import numpy as np
import math


# utility function to calculate slopes for stock prices using linear regression method
def linear_regression(prices):
    days = [5, 4, 3, 2, 1]
    sum_x_list = []
    x_sqr_list = []
    sum_xy_list = []
    sum_xy = 0

    for i in range(len(prices)):
        stock_prices = list(prices[i])
        # print(stock_prices)
        sum_x = sum(stock_prices)
        sqr_stock_prices = list(np.array(stock_prices)**2)
        sum_sqr_x = sum(sqr_stock_prices)
        for j in range(5):
            sum_xy += stock_prices[j]*days[j]
        sum_xy_list.append(sum_xy)
        sum_x_list.append(sum_x)
        x_sqr_list.append(sum_sqr_x)
    # print(sum_x_list)
    # print(sum_xy_list)
    # print(x_sqr_list)

    # calculate slope for each stock using slope formula for linear regression
    # sum of days is 15
    for i in range(len(sum_xy_list)):
        slopes.append((5*sum_xy_list[i] - 15*sum_x_list[i])/(5*x_sqr_list[i] - sum_x_list[i]**2))
    # print(slopes)


# main function that prints the transactions
def printTransactions(m, k, d, name, owned, prices):
    money_available = m
    transactions = []
    stock_count = 0

    print(m)
    print(k)
    print(d)
    print(name)
    print(owned)

    # sell all stocks with decreasing prices
    for h in range(k):
        if slopes[h] < 0 and owned[h] > 0:
            transactions.append(name[h] + " SELL " + str(owned[h]))
            owned[h] = 0

    # buy stocks that show an increasing trend in prices
    for j in range(len(prices)):
        stock_prices = np.array(prices[j])
        while slopes[j] > 0 and money_available >= stock_prices[4]:
            money_available -= stock_prices[4]
            owned[j] += 1
            stock_count += 1
        transactions.append(name[j] + " BUY " + str(stock_count))

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

slopes = []

linear_regression(prices)
printTransactions(m, k, d, name, owned, prices)
