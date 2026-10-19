class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key = lambda a : a[0])
        skipped = 0
        
        lastEnd = sortedIntervals[0][1]
        for i in range(1, len(sortedIntervals)) : 
            if lastEnd > sortedIntervals[i][0] : 
                skipped += 1
                lastEnd = min(lastEnd,  sortedIntervals[i][1])
            else : 
                lastEnd = sortedIntervals[i][1]
        
        return skipped
            

        