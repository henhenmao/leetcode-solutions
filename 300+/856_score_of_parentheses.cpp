
/*
856. Score of Parentheses (https://leetcode.com/problems/score-of-parentheses/description/?envType=daily-question&envId=2026-10-04)

keep track of the 'layer' that a closing bracket ends at

the score of a single pair of closing parentheses depend on the layer, or the size of the stack when counting parentheses
  score += 2^layer, with the first layer of parentheses being at layer 0

iterate through the parentheses string with index i, let c = s[i]
  if c == '(', then increment the layer and move onto i++

  if c == ')', then we need to make one more check

    we need to check s[i-1] (which will always exist as a ')' is guaranteed to have at least one '(')
      if s[i-1] is a ')', then we do not add anything, as we can be sure that this pair of parentheses is just a multiplier
      otherwise, we can add to the score 2^layer
    after this check, we can decrement the layer by 1 as this pair of parentheses has been closed
    
runtime: O(n) where n is the size of s
space: O(1)
*/

#include <iostream>
#include <cmath>
using namespace std;

int scoreOfParentheses(string s) {
  int score = 0;
  int layer = -1;
  int n = s.length();

  for (int i = 0; i < n; i++) {
    char c = s[i];

    // cout << "index " << i << " at layer " << layer << endl; 

    if (c == '(') {
      layer++;
    } else {
      if (s[i-1] == '(') {
        score += pow(2, layer);
      }
      layer--;
    }
  }

  return score;
}

// int main() {
//   string s = "(())()";
//   cout << scoreOfParentheses(s) << endl;
//   return 0;
// }