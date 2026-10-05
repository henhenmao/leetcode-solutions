
/*
678. Valid Parenthesis String (https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2026-10-04)

  variant of 20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/description/)
    string only contains '(' and ')' parentheses
    '*' character is a placeholder for either '(' or ')'

  if a '*' is encountered:
    if the stack is empty (no unclosed parentheses), then '*' cannot be a ')', and must be '(' or empty
    if the stack is nonempty (unclosed parentheses), then '*' can be either '(', ')', or empty

  use recursive backtracking to find various parentheses strings when faced with multiple choices of '*'
  the dp state depends on i, the index of string s, and p, the number of unclosed '(' in out stack
  
  note: since this question only deals with '(' and ')', we can just use int p instead of a stack,
    where p is the number of unclosed '(' in the 'stack'
      the original question needs a stack because there were three different types of parentheses to keep track of

  time complexity: O(n^2) where n is the size of s
  space complexity: O(n^2), because of the n*n dp table


*/

#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int paras(int i, string& s, int p, vector<vector<int>>& dp) {
    if (p < 0) return false;
    if (i >= s.length()) return (p == 0);
    if (dp[i][p] != -1) return dp[i][p];

    char c = s[i];
    bool res = false;
    
    if (c == '(') {
        res = paras(i+1, s, p+1, dp);
    } else if (c == ')') {
        res = (p > 0) && paras(i+1, s, p-1, dp);
    } else {
        res = paras(i+1, s, p+1, dp) || paras(i+1, s, p-1, dp) || paras(i+1, s, p, dp);
    }

    dp[i][p] = res;
    return res;
}

bool checkValidString(string s) {
    int n = s.length();
    vector<vector<int>> dp((n+1), vector((n+1), -1));
    return paras(0, s, 0, dp);
}

// int main() {
//   return 0;
// }