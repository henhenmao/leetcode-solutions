

from typing import Optional

"""
1339. Maximum Product of Splitted Binary Tree (https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/?envType=daily-question&envId=2026-01-07)

at any one node, how do we split the tree from that node and calculate the sum products?

keep in mind that if we first store the total sum of the tree somewhere, once we find the sum of one subtree, we can get the sum of the second tree as well
    1. do a full traversal of tree to get the total sum of the tree
    2. for each node, store the sums of the subtrees of that node, both the left and the right subtree. use dfs to do this

at each given node root, obtain (subtree sum of root.left) and (subtree sum of root.right)
then you need to decide which subtree the root should be a part of

let treeSum = sum of all nodes in the tree
let root = the current node in a recursive function
let curr = root.val
let left = sum of the left subtree of root
let right = sum of the right subtree of root

we need to consider each node as the root of a subtree
    at any given node, treat it as the root of a subtree with the sum of (curr + left + right)
    the product sum with this split can then be calculated as:

    productSum = (curr + left + right) * (treeSum - curr - left - right)

runtime: O(n) where n is the number of nodes in the tree
space: O(logn)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxProduct(root: Optional[TreeNode]) -> int:

    treeSum = 0
    MOD = 1e9+7

    def getTreeSum(root):
        if not root:
            return 0
        total = root.val
        total += getTreeSum(root.right)
        total += getTreeSum(root.left)
        return total

    treeSum = getTreeSum(root)

    maxProduct = float('-inf')

    def subtreeSums(root):
        nonlocal treeSum
        nonlocal maxProduct

        if not root:
            return 0
        
        curr = root.val
        left = subtreeSums(root.left)
        right = subtreeSums(root.right)
        total = curr + left + right

        currProduct = (total) * (treeSum - total)
        maxProduct = max(maxProduct, currProduct)

        return total
    
    subtreeSums(root)
    return int(maxProduct % MOD)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print(maxProduct(root))


