
#include <stdio.h>
#include <stdlib.h>

/*
1385. Find the Distance Value Between Two Arrays (https://leetcode.com/problems/find-the-distance-value-between-two-arrays/?envType=daily-question&envId=2026-11-05)

just use a double loop
  for each element arr1[i], loop over all arr2[j], and if abs(arr1[i] - arr2[j]) <= d for any j,
  arr1[i] is not valid and does not count towards the total

runtime: O(n*m), n is length of arr1, m is length of arr2
space: O(1)
*/

int validElement(int* arr1, int arr1Size, int* arr2, int arr2Size, int d, int i) {
    for (int j = 0; j < arr2Size; j++) {
        if (abs(arr1[i]-arr2[j]) <= d) return 0;

    }
    return 1;
}

int findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size, int d) {
    int count = 0;
    for (int i = 0; i < arr1Size; i++) {
        count += validElement(arr1, arr1Size, arr2, arr2Size, d, i);
    }
    return count;
}