class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        multi = 1
        for i in range(len(nums) - 1) :
            multi *= nums[i]
            ans[i+1] = multi

        multi = 1
        for i in range(len(nums)-1,0,-1) : 
            multi *= nums[i]
            ans[i-1] *= multi

        return ans


            

