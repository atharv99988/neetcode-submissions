# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(node, level):
    if not node :
        return 0 
    else : 
        left_depth = depth(node.left, level)
        right_depth = depth(node.right, level)
        return max(left_depth, right_depth) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depth(root, 0)
        