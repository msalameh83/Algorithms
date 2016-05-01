__author__ = 'Mohammad'


import sys


"""
Top down dynamic programing. Using map to store intermediate results.
Returns Integer.MAX_VALUE if total cannot be formed with given coins
https://www.youtube.com/watch?v=Kf_M7RdHr1M&feature=youtu.be
"""
def min_coin_top_down(total, coin, chart):
    if total == 0 :
        return 0
    if total in chart:
        return chart[total]
    min_val = sys.maxsize
    for i in range(len(coins)):
        if coin[i] > total:
            continue
        val = min_coin_top_down(total - coin[i], coins, chart)

        # if val we get from picking coins[i] as first coin for current total is less
        # than value found so far make it minimum.
        if val  < min_val:
            min_val = val
    # if min is MAX_VAL dont change it. Just result it as is. Otherwise add 1 to it.
    if min_val != sys.maxsize:
        min_val = min_val + 1

    # memoize the minimum for current total.
    chart[total] = min_val

    return min_val
# ----------------------------------------------------------------------------
# BUTTOM UP APPROACH
# O(total x coins)


def print_coin_combination(R, coins):
    if R[-1] == -1:
        print('No Solution')
    start = len(R) -1
    comb = []
    while start != 0:
        j = R[start]
        comb.append(coins[j])
        start = start - coins[j]
    print ("Combination is: %s "%comb)

def minimum_coin_bottom_up(total, coins):
    T = [sys.maxsize]*(total+1)
    R = [-1]*(total+1)
    T[0] = 0

    for j in range(len(coins)):
        for i in range(1, total + 1):
            if i - coins[j] < 0:continue
            if  T[i - coins[j]] + 1 < T[i]:
                T[i] = T[i - coins[j]] + 1
                R[i] = j


    print (T)
    print(R)
    print_coin_combination(R, coins)
    return T[-1]







coins = [1, 2, 4, 8]
total = 11
chart = {}
print("%d"%min_coin_top_down(total, coins,chart))


coins = [7, 2, 3, 6]
total = 13
chart = {}
print("%i"%minimum_coin_bottom_up(total, coins))


