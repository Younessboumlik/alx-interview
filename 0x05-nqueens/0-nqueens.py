#!/usr/bin/python3
""" This program is solving the Nqueens problem using backtracking """


def solvenqueens(n):
    """ This is the main function that will solve the n queens problem. """
    if(type(n) != int):
        print("N must be a number")
        exit(1)
    elif (n < 4):
        print("N must be at least 4")
        exit(1)
    result = []
    solutions = []
    solvingnqueens(n, 0, result, solutions)
    return solutions

def solvingnqueens(n,row,result,solutions):
    """ This function will solve the n queens problem recursively using backtracking. """
    if(row == n):
        solutions.append(result[:])
        return
    for col in range(n):
        if(issafe(row, col, result)):
            result.append([row, col])
            solvingnqueens(n, row + 1, result, solutions)
            result.pop()
    pass

def issafe(row, col, result):
    """ This function will check if a queen can be placed at a given position. """
    for i in range(len(result)):
        if(result[i][1] == col or result[i][0] == row or abs(result[i][0] - row) == abs(result[i][1] - col)):
            return False
    return True




# if __name__ == "__main__":
#     solutions = solvenqueens('d')
#     print(solution)
#     solutions = solvenqueens(2)
#     print(solution)
#     solutions = solvenqueens(6)
#     print(solution)
