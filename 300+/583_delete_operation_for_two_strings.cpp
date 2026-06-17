


/*
583. Delete Operation for Two Strings (https://leetcode.com/problems/delete-operation-for-two-strings/description/?envType=problem-list-v2&envId=dynamic-programming)

essentially the same solution as 1143. Longest Common Subsequence (https://leetcode.com/problems/longest-common-subsequence/description/)

compare the first character of each string
if they are the same: return 1 + longestCommonSubsequence(text1[1:], text2[1:])
if they are different: return max(longestCommonSubsequence(text1[1:], text2), longestCommonSubsequence(text1, text2[1:]))
once one of the two strings becomes length 0, return

DO NOT CREATE A NEW SUBSTRING AT EACH RECURSIVE CALL
    JUST USE TWO POINTERS
    each pointer represents the beginning index for each "substring"

the end result of the minimum delete operations for two strings always results in both strings becoming the longest common subsequence
    let lcs = the length of the longest common subseqeunce of word1 and word2
    we can simply subtract (word1.length() + word2.length()) by (lcs * 2) to get the number of deleted characters

runtime of getting the longest common subseqeunce: O(n * m) where n and m are the lengths of word1 and word2

runtime: O(n * m) where n and m are the lengths of word1 and word2
space: O(n * m)
*/


#include <iostream>
#include <vector>
using namespace std;

int helper(string& word1, string& word2, int i, int j, vector<vector<int>>& dp) {
    if (i == word1.length() || j == word2.length()) {
        return 0;
    }

    if (dp[i][j] != -1) {
        return dp[i][j];
    }

    int largest = 0;
    if (word1[i] == word2[j]) {
        largest = 1 + helper(word1, word2, i+1, j+1, dp);
    }

    largest = max(largest, max(helper(word1, word2, i+1, j, dp), helper(word1, word2, i, j+1, dp)));

    dp[i][j] = largest;
    return dp[i][j];
}

int minDistance(string word1, string word2) {
    int totalLength = word1.length() + word2.length();
    vector<vector<int>> dp(word1.length()+1, vector<int>(word2.length()+1, -1));
    int minOperations = totalLength - 2 * helper(word1, word2, 0, 0, dp);
    return minOperations;
}


int main() {
    string word1 = "sea";
    string word2 = "eat";
    cout << minDistance(word1, word2) << endl;
    return 0;
}