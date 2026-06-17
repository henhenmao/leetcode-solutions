

/*
396. Rotate Function (https://leetcode.com/problems/rotate-function/description/?envType=problem-list-v2&envId=dynamic-programming)

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]

example: nums = [1,2,3,4]

F(0) = (0 * 1) + (1 * 2) + (2 * 3) + (3 * 4) = 20
F(1) = (0 * 4) + (1 * 1) + (2 * 2) + (3 * 3) = 14
F(2) = (0 * 3) + (1 * 4) + (2 * 1) + (3 * 2) = 12
F(3) = (0 * 2) + (1 * 3) + (2 * 4) + (3 * 1) = 14
F(0) has the maximum value

let's focus on jsut F(0) and F(1)
F(0) = (0 * 1) + (1 * 2) + (2 * 3) + (3 * 4) = 20
F(1) = (0 * 4) + (1 * 1) + (2 * 2) + (3 * 3) = 14

from the sum of F(0), we essentially do the following
- add 1 once (0 * 1) -> (1 * 1)
- add 2 once (1 * 2) -> (2 * 2)
- add 3 once (2 * 3) -> (3 * 3)
- remove 4 three times (3 * 4) -> (0 * 4)

when going from F(k) to F(k+1), we are removing arr_k[-1] (len(nums)-1) times while adding every other number once

let n = len(nums), let sum = sum(nums), let last = the last element of arr_k
    F(k+1) = F(k) - ((n-1) * curr) + (sum - curr)

    this formula basically simulates the last element wrapping back to being multiplied by zero, while every other number gets added once since they rotate up

calculate F(0) manually and then calculate each instance of F(k) based off of the sum of F(k-1)

runtime: O(n) where n is the length of nums
space: O(n)
*/

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int fzero(vector<int>& nums) {
    int total = 0;
    for (int i = 0; i < nums.size(); i++) {
        total += (i * nums[i]);
    }
    return total;
}

int maxRotateFunction(vector<int>& nums) {
    int n = nums.size();
    int sum = accumulate(nums.begin(), nums.end(), 0);
    int last = n-1;

    vector<int> res(n, 0);

    // first calculate F(0)
    res[0] = fzero(nums);

    // apply the formula for each instance of F(k)

    for (int i = 1; i < n; i++) {
        res[i] = res[i-1] - ((n-1) * nums[last]) + (sum - nums[last]);
        last -= 1;
    }

    return *max_element(res.begin(), res.end());
}


int main() {

    vector<int> nums = {4,3,2,6};

    cout << maxRotateFunction(nums) << endl;

    return 0;
}