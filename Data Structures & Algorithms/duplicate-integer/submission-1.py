class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dublicates = set()
        for num in nums : 
            if num in dublicates : 
                return True
            else : 
                dublicates.add(num)

        return False
        
        