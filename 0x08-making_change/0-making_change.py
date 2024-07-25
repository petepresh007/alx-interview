#!/usr/bin/python3

""" a module for makechange"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    chng = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            chng += 1
        if (total == 0):
            return chng
    return -1
