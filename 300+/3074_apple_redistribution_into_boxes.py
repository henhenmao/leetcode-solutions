

from typing import List

"""
3074. Apple Redistribution into Boxes (http://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24)

Note that, apples from the same pack can be distributed into different boxes.

theres literally no constraint at all in how we can organize the apples into boxes
    our sole goal is to just cram every single apple into a box somehow, while minimizing the amount of boxes used

given this, there is no reason why we shouldn't just always pick the largest box we have available

algorithm:
    1. sort the capacity array in non-decreasing order
    2. count the total number of apples we need to store
    3. pop the last (largest) box from the end of the capacity array
    4. subtract that capicity from the the total number of apples
    5. if the total number of apples remaining to be stored is less than or equal to zero, return the number of boxes used

runtime: O(mlogm + n), where m is the length of the capacity array and n is the length of apples
space: O(1)
"""

def minimumBoxes(apple: List[int], capacity: List[int]) -> int:

    capacity.sort()
    remaining = sum(apple)
    boxesUsed = 0

    while remaining > 0:
        remaining -= capacity.pop()
        boxesUsed += 1

    return boxesUsed

