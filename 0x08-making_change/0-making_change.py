#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total. """
def makeChange(coins, total):
    """Return the minimum number of coins needed to make change for total."""
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    n = 0
    for coin in coins:
        while total >= coin:
            n += total // coin
            total = total % coin
            if(total == 0):
                return n
    return -1
