class Solution:
    def rob(self, array: List[int]) -> int:
        if not len(array):
            return 0
        elif len(array) == 1:
            return array[0]

        max_sum = array.copy()
        max_sum[1] = max(array[0], array[1])

        for i in range(2,len(max_sum)):
            max_sum[i] = max(max_sum[i-1], max_sum[i-2] + array[i])
        return max_sum[-1]