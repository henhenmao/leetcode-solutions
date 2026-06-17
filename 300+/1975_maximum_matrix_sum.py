
from typing import List

"""
1975. Maximum Matrix Sum (https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05)

imagine a 1d array instead of a 2d matrix, with the same available operation
    can multiply two adjacent elements by -1

1. single negative in 1d array
let nums = [-5,4,3,2,1]

in this case, we intuitively want to move the negative sign from -5 to -1 to maximize the sum of the array
    using the operation, we can "shift" the negative sign left or right however we want

nums = [-5,4,3,2,1]
nums = [5,-4,3,2,1]
nums = [5,4,-3,2,1]
nums = [5,4,3,-2,1]
nums = [5,4,3,2,-1] (yay!)

when there is a single negative in a row, your best option is to just move the negative to the smallest element

2. even negatives in 1d array
let nums = [-5,4,-3,2,1]

if there are an even number of negatives in a row, we can "shift" a negative until the two negatives are adjacent
    once they are adjcent you can remove the negative sign from both of them
    as long as the row has an even number of initial negative numbers, you can cancel out all of them with enough operations

nums [-5,-4,3,2,1]
nums [5,4,3,2,1] (yay!)

3. odd negatives in 1d array
let nums [-5,4,-3,-2,1]

if there are an odd number of negatives in a row, we can continue to cancel out pairs of elements until one remains
once we do that we simply move the negative to the smallest element in the array

4. translating everything above to 2d matrix

in a 2d matrix, we can do our operation on any two adjacent elements
this means we have free reign on shifting negatives across rows and columns

this allows us to conclude that
    - if there are initially an even number of negatives in the matrix, we are able to remove every negative
        the result will be the sum of the absolute value of each element

    if there are initially an odd number of negatives in the matrix, we are able to remove every negative except for one
        the result will be (the sum of the absolute value of each element) - (2 * the absolute value of the smallest magnitude element)
        we multiply by 2 because the element is 1) excluded from the sum and 2) subtracted again because of the negative sign

runtime: O(n^2) where n is the length and width of the matrix
space: O(1)
"""

def maxMatrixSum(matrix: List[List[int]]) -> int:

    neg_count = 0
    smallest_element = abs(matrix[0][0])
    total_sum = 0

    for row in matrix:
        for num in row:
            if num < 0:
                neg_count += 1
            smallest_element = min(smallest_element, abs(num))
            total_sum += abs(num)

    if neg_count % 2 == 0:
        return total_sum
    else:
        return total_sum - (2 * smallest_element)


