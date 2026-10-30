class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i in range(len(nums) - 2) : 
            
            if i and nums[i] == nums[i - 1]:
                continue
            
            j = i+1
            k = len(nums) - 1
            while j < k : 

                total = nums[i] + nums[j] + nums[k]
                if total == 0 : 
                    triplets.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total > 0 : 
                    k -= 1
                else : 
                    j += 1
        
        return triplets
                

        