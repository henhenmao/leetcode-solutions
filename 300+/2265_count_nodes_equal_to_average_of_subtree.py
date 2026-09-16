

"""
2265. Count Nodes Equal to Average of Subtree (https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2026-09-10)

dfs traversal of the tree allows you to check the average of each node's subtree
to get the subtree average you need:
  1. the sum of the subtree (including current node)
  2. the total nodes in the subtree (including current node)

each node will return these two values
  1. sum of left subtree + sum of right subtree + current value
  2. total nodes in left subtree + sum of right subtree + 1

runtime: O(n) where n is the number of nodes
space: O(h) where h is the height of the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfSubtree(root: TreeNode) -> int:
  res = 0
  def dfs(curr):
      nonlocal res
      if not curr:
          # return (sum, count)
          return 0, 0

      left_sum, left_count = dfs(curr.left)
      right_sum, right_count = dfs(curr.right)
      subtree_avg = (left_sum + right_sum + curr.val)//(left_count + right_count+1)

      if subtree_avg == curr.val:
          res += 1

      return (left_sum + right_sum + curr.val), (left_count + right_count + 1)

  dfs(root)
  return res