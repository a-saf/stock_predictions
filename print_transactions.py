import numpy as np
import math

# get and sanitize input
line_one = input()
list_one = line_one.split(" ", 1)
m = float(list_one[0])
k = int(list_one[1])
d = int(list_one[2])
name = []
owned = []
prices = []

for i in range(k):
    stock_info = input()
    stock_list = stock_info.split(" ", 1)
    name[i] = stock_list[0]
    owned[i] = int(stock_list[1])
    prices.append(float(i) for i in stock_list[2:7])

slopes = []


def linear_regression(prices):
    days = [5, 4, 3, 2, 1]
    sum_xy = 0
    sum_x = 0
    sum_sqr_x = 0
    sum_x_list = []
    x_sqr_list = []
    sum_xy_list = []

    for x in range(k):
        for y in range(5):
            xy = prices[x][y]*days[y]
            sum_xy += xy
            sum_x += prices[x][y]
            sum_sqr_x += pow(prices[x][y], 2)
        sum_xy_list[x] = sum_xy
        sum_x_list[x] = sum_x
        x_sqr_list[x] = sum_sqr_x

    # calculate slope for each stock using slope formula for linear regression
    # sum of y values which are the days is 15
    for n in range(k):
        slopes[n] = (5*sum_xy_list[n] - sum_x_list[n]*15)/(5*x_sqr_list[n] - pow(sum_x_list[n], 2))


def printTransactions(m, k, d, name, owned, prices):
    money_available = m
    


