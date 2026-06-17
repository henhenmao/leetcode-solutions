

/*
852. Peak Index in a Mountain Array (https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=study-plan-v2&envId=binary-search)
Your task is to solve it in O(log(n)) time complexity.

let p = the index of the peak element of the mountain array
    arr[p] is the only element in which arr[p] > arr[p-1] and arr[p] > arr[p+1]
    if this condition is true at arr[i], you know i is the peak index


left side of the peak -> values increasing
    arr[i-1] < arr[i] < arr[i+1]
    or i == 0

right side of the peak -> values decreasing
    arr[i-1] > arr[i] > arr[i+1]
    or i == arr.size()-1

edge cases:
    peak is at the very leftmost or very rightmost element
    just use two if cases to handle these two cases
    if the second element is less than the first element, you know that the entire array must be descending
    if the second last element is less than the last element, you know that the entire array must be ascending

other than that just use a binary search to find the peak

runtime: O(logn) where n is the length of arr
space: O(n)
*/

#include <iostream>
#include <vector>
using namespace std;

int peakIndexInMountainArray(vector<int>& arr) {
    
    int n = arr.size();
    int low = 0, high = n-1;

    // handling edge case where peak is at the very edge
    // arr.size() is at least 3
    if (arr[0] > arr[1]) return 0;
    if (arr[n-1] > arr[n-2]) return n-1;

    int mid = (low+high)/2;

    while (low <= high) {
        mid = (low+high)/2;

        if (mid == 0 || (arr[mid-1] < arr[mid] && arr[mid] < arr[mid+1])) { // left side of peak
            low = mid+1;  
            continue;
        } 

        if (mid == n-1 || (arr[mid-1] > arr[mid] && arr[mid] > arr[mid+1])) { // right side of peak
            high = mid-1;
            continue;
        }

        return mid;
    }

    return -1;
}


int main() {
    vector<int> arr = {18,29,38,59,98,100,99,98,90};
    cout << peakIndexInMountainArray(arr) << endl;
    return 0;
}