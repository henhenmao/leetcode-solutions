

/*
1807. Evaluate the Bracket Pairs of a String (https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/?envType=daily-question&envId=2026-10-02)

just iterating over the string with nested while loops controlling the same index
outer while loop increments over s with index i < s.length() and adds every character that isn't a '(' into the result
when a '(' is encounted, we enter the inner while loop, which starts where the outer loop left off and increments index i
  inner loop does the same thing as the outer loop, but keeps track of the substring it goes through, and checks for a ')' to break out
  when we break out of the inner loop, we have kept track of the substring inside the opening and closing parentheses, so we check if the substring
  exists as a key in the knowledge input

runtime: O(n+k) where n is the length of s, and k is the number of characters in knowledge
space: O(n+k)
*/


#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

string evaluate(string s, vector<vector<string>>& knowledge) {
  unordered_map<string, string> map;

  for (const auto& pair : knowledge) {
      map[pair[0]] = pair[1];
  }


  string res = "";
  int n = s.length();
  int i = 0;
  
  while (i < n) {
      char curr = s[i];
      if (curr != '(') {
          res += curr;
          i++;
          continue;
      }

      string key = "";
      while (i < n) {
          i++;
          curr = s[i];
          if (curr != ')') {
              key += curr;
              continue;   
          }

          break;
      }

      if (map.find(key) == map.end()) {
          res += "?";
      } else {
          res += map[key];
      }

      i++;
  }

  return res;
}