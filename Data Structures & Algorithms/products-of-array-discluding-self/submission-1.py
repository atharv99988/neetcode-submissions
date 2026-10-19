class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        temp = 1
        for i in range(1, len(nums)) :
            temp *= nums[i-1]
            ans[i] = temp

        temp = 1

        for j in range(len(nums)-2,-1,-1) :
            temp *= nums[j+1]
            ans[j] *= temp
        
        return ans

