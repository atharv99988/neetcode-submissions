class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculating distance and saving it in form of a tuple
        k_close = [
            (
                math.pow(x, 2) + math.pow(y, 2),
                x,
                y
            ) for x,y in points
        ]

        heapq.heapify(k_close)

        ans = []
        for _ in range(k) :
            points = heapq.heappop(k_close)
            ans.append([points[1],points[2]])
        
        return ans

        
