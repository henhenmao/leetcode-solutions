
import bisect

"""
3720. Lexicographically Smallest Permutation Greater Than Target (https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-27)

construct the resulting permutation string from the available letters of string s
  for character res[i], greedily grab the smallest character that is strictly greater than target[i]
    starting from i = 0, if res[i] can be equal to target[i], always choose that character
    otherwise choose the smallest character res[i] that is strictly greater than target[i]
      use bisect_right to find first index where res[i] is strictly larger than target[i]

  once a character res[i] is chosen to be greater than target[i], all remaining characters res[j] where j > i do not matter anymore since
  the choosing of res[i] makes res lexicographically greater than target no matter what follows
    therefore we can just append the remaining characters to the result in non decreasing order (to make string as small as possible)
"""

def lexGreaterPermutation(s: str, target: str) -> str:
  n = len(s)
  res = ""
  available = sorted(s)

  for tc in target: # find res[i] >= tc
    i = bisect.bisect_left(available, tc)
    if i < n and available[i] == tc:
      available = available[:i] + available[i+1:]
      res += tc
      continue

    if available[-1] < tc:
      return ""
    
    i = bisect.bisect_right(available, tc)
    res += available[i]
    available = available[:i] + available[i+1:]
    res += "".join(available)

    return res if res != target else ""

  return res if res != target else ""
  


s = "a"
target = "b"
print(lexGreaterPermutation(s, target))





