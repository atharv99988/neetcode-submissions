# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        def maxSum(node) :
            if not node : 
                return 0
            
            maxSumLeft = max(maxSum(node.left), 0) # gets rid of left subtree if sum is negative
            maxSumRight = max(maxSum(node.right), 0) # gets rid of right subtree if sum is negative

            ans[0] = max(ans[0], node.val + maxSumLeft + maxSumRight)

            return  node.val + max(maxSumLeft, maxSumRight)

        maxSum(root)
        return ans[0]
