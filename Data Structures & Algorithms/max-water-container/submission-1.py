class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # when to shift left pointer
        area = 0
        l,r = 0, len(heights)-1

        while l < r : 
            temp_area = min(heights[l], heights[r]) * (r-l)
            area = max(temp_area, area)
            if heights[r] > heights[l] : 
                l += 1
            else : 
                r -= 1
        
        return area

        