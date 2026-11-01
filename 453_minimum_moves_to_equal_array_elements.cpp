
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


/*
453. Minimum Moves to Equal Array Elements (https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/?envType=daily-question&envId=2026-11-01)

in one move, you can increment (n-1) elements of the array by 1
ex. nums = [1,2,3,4,5], increment every nums[i] except for nums[0] -> nums = [1,3,4,5,6]

notice that the number of moves to equal array elements depends on the relative distance
between numbers
  ex. the minimum moves to make all array elements equal for nums = [1, 2, 3] and nums = [101, 102, 103] are the same
  thus, we can see that incrementing (n-1) elements does the same thing as decrementing 1 element
    as the relative distance of all elements to each other remain the same

the solution is very simple once we see this

solution:
  1. get the minimum value of nums (if we are decrementing, we aim for all elements to equal min(nums)
    to get the minimum number of decrements)
  2. loop over all elements in nums
  3. if (nums[i] > min(nums)), then add their difference (number of decrements) to a counting total
    otherwise, continue. we simply don't decrement nums[i]

runtime: O(n) where n is the size of nums
space: O(1)
*/

int minMoves(vector<int>& nums) {
  int min = *min_element(nums.begin(), nums.end());
  int moves = 0;
  for (int n: nums) {
      if (n > min) moves += (n - min); 
  }
  return moves;
}