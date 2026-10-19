class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        sum = 0
        for i in nums : 
            if sum < 0 : 
                sum = 0
            sum += i
            ans = max(ans, sum)
        return ans

        