

"""
2483. Minimum Penalty for a Shop (https://leetcode.com/problems/minimum-penalty-for-a-shop/description/?envType=daily-question&envId=2025-12-26)

we want to minimize the penalty, which is increased by the following
1. N appearing before closing
2. Y appearing after closing

note that penalty is unaffected by a Y appearing before closing or a N appearing after closing
    we are focused on minimizing the penalty so just the above two cases

this means we are trying to find the proper split in the list
    let L = the left partition (hours when the shop is open)
    let R = the right partition (hours when the shop is closed)

penalties:
    "N" appearing in L
    "Y" appearing in R

we want to find the proper partition index where the sum of the two above cases is minimized 

we can use prefix and suffix sum arrays to efficiently compute the number of N's appearing before closing and the number of Y's appearing after closing
    use a prefix sum array to compute the number of N's that appear before each index
    use a suffix sum array to compute the number of Y's that appear after each index

note: if a shop closes at the jth hour, the shop is closed on hour j
    this means that for our suffix sum array, we want to include index i into the ith suffix sum
    but we do not include index i into the ith prefix sum

once we have both the prefix and suffix sum arrays, we simply just search for the proper index i, where prefix[i]+suffix[i] is minimized
    i will be the hour that you close to minimize the total penalty
    oh yeah and we want the earliest hour so when iterating across both arrays for the minimum sum, don't update your final result if equal

runtime: O(n) where n is the length of customers
space: O(n)
"""

def bestClosingTime(customers: str) -> int:

    n = len(customers)

    opened = [0] * (n+1)
    closed = [0] * (n+1)

    nCount = 0
    for i in range(n):
        opened[i] = nCount
        if customers[i] == "N":
            nCount += 1
    opened[n] = nCount
    
    yCount = 0
    for i in range(n-1, -1, -1):
        if customers[i] == "Y":
            yCount += 1
        closed[i] = yCount

    bestHour = 0
    minPenalty = opened[0] + closed[0]
    for i in range(len(opened)):
        currPenalty = opened[i] + closed[i]

        if minPenalty > currPenalty:
            minPenalty = currPenalty
            bestHour = i

    return bestHour


customers = "YYNY"
print(bestClosingTime(customers))

