
from typing import List

"""
3483. Unique 3-Digit Even Numbers (https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11)

since we are only looking for 3-digit numbers, and 3 <= digits.length <= 10, we can safely use a triple for-loop to brute force all options
things to note:
  1. the leading digit cannot be a zero
  2. that's literally it i think

do a triple for loop to get all size-3 permuations of digits in digits
  if the first digit is a zero, skip it
  if indexes are repeated, skip
  if last digit is odd, skip

put all permutations into a set so that duplicates are removed
return the size of the set at the very end

runtime: O(n^3) where n is the size of digits
space: O(n)
"""

def totalNumbers(digits: List[int]) -> int:
    total = set()
    n = len(digits)
    for i in range(n):
        if digits[i] == 0:
            continue
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue

                if digits[k] % 2 == 1:
                    continue
                total.add(digits[i]*100 + digits[j]*10 + digits[k])
    return len(total)