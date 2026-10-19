class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-cnt, key) for key, cnt in count.items()]
        ans = []
        heapq.heapify(heap)

        for i in range(k) : 
            cnt, key = heapq.heappop(heap)
            ans.append(key)

        return ans


        