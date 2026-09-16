
from typing import List

"""
836. Rectangle Overlap (https://leetcode.com/problems/rectangle-overlap/?envType=daily-question&envId=2026-09-14)

  two rectangles overlap if and only if their x projections overlap AND their y projections overlap well
      if there is a single gap on any axis, they do not overlap

  when is there an overlap?
      take intervals A = [a1, a2], and B = [b1, b2]
      if b1 < a2 (B starts before A ends), there is an overlap
      or if a1 < b2 (A starts before B ends), there is an overlap

  do this check for the y axis as well, and return all four overlap checks being true at the same time

  runtime: O(1)
  space: O(1)

"""

def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    
    ax1, ay1, ax2, ay2 = rec1
    bx1, by1, bx2, by2 = rec2

    return ax1 < bx2 and bx1 < ax2 and ay1 < by2 and by1 < ay2