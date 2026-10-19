class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums : 
            if i not in hash : 
                hash[i] = 1
            else  :
                hash[i] += 1
        
        sorted_items = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        
        # Return the first k elements
        return [num for num, freq in sorted_items[:k]]
        

        
        
        