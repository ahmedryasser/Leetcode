import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for item,count in counts.items():
            heapq.heappush(heap , (count,item))
            if len(heap)>k:
                heapq.heappop(heap)
        return [char for _,char in heap]