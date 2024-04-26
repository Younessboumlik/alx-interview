#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
  
    l = [[1]]
    if n <= 0 :
        return []
    for i in range(1,n):
        l = l + [l[i-1] + [1]]
        j = i - 1
        while j > 0:
            l[i][j] = l[i][j] + l[i][j - 1]
            j -= 1
    return l
