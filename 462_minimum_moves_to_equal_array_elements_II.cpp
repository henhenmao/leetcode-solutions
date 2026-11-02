
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
462. Minimum Moves to Equal Array Elements II (https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/?envType=daily-question&envId=2026-11-02)



with both increments and decrements, setting the array to equal the median of the initial array
is always the most optimal path 

sort the array first so that we can get the median

if n = nums.size() is odd -> there is one median at nums[n/2]
  loop over every element of nums
    the number of moves to get nums[i] to median is abs(median - nums[i])
  sum the total


if n = nums.size() is even -> there are two medians at nums[n/2 - 1] and nums[n/2]
  loop over every element of nums and count the number of moves for both medians
  compare both median's number of moves and return the minimum

runtime: O(n * log(n)) where n is the size of the array
space: O(1)
*/

int minMoves2(vector<int>& nums) {
  int n = nums.size();
  int moves = 0;
  sort(nums.begin(), nums.end());


  // if size of nums is odd -> one median
  if (n % 2 == 1) {
      int median = nums[n/2];
      for (int num : nums) {
          moves += abs(num - median);
      }
      return moves;
  }

  // if size of nums even -> check both medians
  int median1 = nums[n/2 - 1];
  int median2 = nums[n/2];
  int moves1 = 0, moves2 = 0;
  for (int num : nums) {
      moves1 += abs(num - median1);
      moves2 += abs(num - median2);
  }
  return min(moves1, moves2);
}