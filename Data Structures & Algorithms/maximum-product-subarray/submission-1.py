class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmin,currmax = 1,1

        for n in nums : 
            
            temp = currmax*n
            currmax = max(currmax*n, currmin*n, n)
            currmin = min(currmin*n, temp, n)
            res = max(res, currmax)

        return res
        