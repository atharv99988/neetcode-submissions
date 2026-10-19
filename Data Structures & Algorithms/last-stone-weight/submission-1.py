class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1 : 
            first_stone = -1 * heapq.heappop(heap)
            second_stone = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -(first_stone-second_stone))

        return abs(heap[0]) if len(heap) == 1 else 0


        