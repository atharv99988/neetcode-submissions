class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_range = len(nums)
        xor_array = 0

        for i in nums : 
            xor_array = i ^ xor_array

        for i in range(len(nums)) : 
            xor_range = xor_range ^ i

        return xor_range ^ xor_array
        