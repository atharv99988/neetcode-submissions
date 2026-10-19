# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        i = [0]
        def dfs(node) :
            if not node : 
                return 
            
            dfs(node.left)
           
            i[0] += 1
            if i[0] == k : 
                ans[0] = node.val
                return 
                
            dfs(node.right)

        dfs(root)
        return ans[0]

        