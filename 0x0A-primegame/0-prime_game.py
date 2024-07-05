#!/usr/bin/python3
""" Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n,they take turns choosing a
prime number from the set and removing that number and its
multiples from the set. The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is. """


def isPrime(num):
    """ check if a number is prime"""
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def isWinner(x, nums):
    """ determine the winner of the game"""
    maria = 0
    ben = 0
    for i in range(x):
        n = 0
        for j in range(1, nums[i] + 1):
            if isPrime(j):
                n += 1
        if n % 2 == 0:
            ben += 1
        else:
            maria += 1
        
    return "Maria" if maria > ben else  "Ben"

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
