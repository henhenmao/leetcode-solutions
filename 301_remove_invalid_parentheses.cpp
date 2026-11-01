
/*
301. Remove Invalid Parentheses (https://leetcode.com/problems/remove-invalid-parentheses/description/?envType=daily-question&envId=2026-10-04)

literally just choose unchoose the brackets when appropiate and prune cases that don't work
my code is very messy and i don't think its even optimal

runtime: O(2^n) where n is the size of s
space: O(n)
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

void genPara(string& s, string& curr, int i, int unopened, int skipped, int& minSkipped, vector<string>& res, unordered_set<string>& visited) {
  if (skipped > minSkipped) return;

  if (i >= s.length()) { // implies current skipped is less than minSkipped
      if (unopened > 0 || visited.find(curr) != visited.end()) return;

      if (skipped == minSkipped){
          res.push_back(curr);
          visited.emplace(curr);
      }
      else {
          minSkipped = skipped;
          visited.clear();
          res.clear();
          res.push_back(curr);
          visited.emplace(curr);
      };
      return;
  }

  char c = s[i];
  if (c != '(' && c !=')') { // letter
      curr.push_back(c);
      genPara(s, curr, i+1, unopened, skipped, minSkipped, res, visited);
      curr.pop_back();
      return;
  }

  if (c == '(') {
      genPara(s, curr, i+1, unopened, skipped+1, minSkipped, res, visited); // skip
      curr.push_back(c);
      genPara(s, curr, i+1, unopened+1, skipped, minSkipped, res, visited);
      curr.pop_back();
  }

  if (c == ')') {
      genPara(s, curr, i+1, unopened, skipped+1, minSkipped, res, visited); // skip

      if (unopened > 0) { // only add c to curr if it is valid
          curr.push_back(c);
          genPara(s, curr, i+1, unopened-1, skipped, minSkipped, res, visited);
          curr.pop_back();
      }
  }

  return;
}

vector<string> removeInvalidParentheses(string s) {
  vector<string> res;
  unordered_set<string> visited;
  int n = s.length();
  string curr = "";
  int minSkipped = n+1;

  genPara(s, curr, 0, 0, 0, minSkipped, res, visited);

  if (res.size() == 0) return {""};

  return res;
}