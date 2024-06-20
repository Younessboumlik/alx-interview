#!/usr/bin/python3
def makeChange(coins, total):
    """Return the minimum number of coins needed to make change for total."""
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    print(coins)
    n = 0
    for coin in coins:
        while total >= coin:
            n += total // coin
            total = total % coin
            if (total == 0):
                return n
    return -1