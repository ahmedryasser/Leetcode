class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i,num in enumerate(nums):
            if len(heap)<k:
                heapq.heappush(heap, (num,i))
            elif num > heap[0][0]:
                heapq.heapreplace(heap, (num,i))
        heap.sort(key= lambda x:x[1])
        return [num for num,_ in heap]