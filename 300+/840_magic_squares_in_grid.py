
from typing import List

"""
840. Magic Squares in Grid (https://leetcode.com/problems/magic-squares-in-grid/?envType=daily-question&envId=2025-12-30)

literally just brute forced checking every 3x3 square in the grid if it is a magic square or not
    remember to ensure that each magic square you check has only numbers 1-9 and also are distinct numbers

runtime: O(n * m) where n and m are the length and width of the grid
space: O(1)
"""


def numMagicSquaresInside(grid: List[List[int]]) -> int:

    def isMagic(g): # takes in a 3x3 section of main grid
        # count rows
        magic = sum(g[0])

        for i in range(3):
            rowSum = g[i][0] + g[i][1] + g[i][2]
            colSum = g[0][i] + g[1][i] + g[2][i]
            if rowSum != magic or colSum != magic:
                return False

        diag1 = g[0][0] + g[1][1] + g[2][2]
        diag2 = g[0][2] + g[1][1] + g[2][0]

        if diag1 != magic or diag2 != magic:
            return False

        return True


    n = len(grid)
    m = len(grid[0])
    count = 0

    for i in range(n-2):
        for j in range(m-2):
            row1 = grid[i][j:j+3]
            row2 = grid[i+1][j:j+3]
            row3 = grid[i+2][j:j+3]
            nums = row1+row2+row3
        
            if len(set(nums)) != 9 or not all(1 <= x <= 9 for x in nums): # magic square must contain distinct numbers
                continue

            g = [row1, row2, row3]

            count += isMagic(g)

    return count
            

grid = [[10,3,5],
        [1,6,11],
        [7,9,2]]
print(numMagicSquaresInside(grid))