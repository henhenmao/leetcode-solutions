
from typing import List

"""
526. Beautiful Arrangement (https://leetcode.com/problems/beautiful-arrangement/description/?envType=problem-list-v2&envId=dynamic-programming)

standard dfs and backtracking algorithm used for permutations 

dfs algorithm:
    1. loop through each number in nums
    2. for each value nums[i], recurse through the possibility of adding nums[i] to the result
    3. backtrack and remove nums[i] from the result because of the possibility of not adding nums[i] to the result
    4. once dfs is over it should have covered all of the possible permutations

at each step of building a permutation, check if the conditions are met:
    perm[i] divisible by i
    or
    i divisible by perm[i]

    since you are building each permutation element by element, you only need to check this for each added element

if the condition is ever broken, immediately backtrack and continue

runtime: O(n!)
space: O(n)
"""

def countArrangement(n: int) -> int:

    res = 0
    used = [False] * (n+1)

    def dfs(i): # curr is current building permutation
        nonlocal res

        # base case: append permutation and return when all nums are used
        if i > n:
            res += 1
            return 

        for j in range(1, n+1):
            if (used[j] == True) or (j % i != 0 and i % j != 0):
                continue

            used[j] = True
            dfs(i+1)
            used[j] = False

    dfs(1)
    return res

n = 2
print(countArrangement(n))



