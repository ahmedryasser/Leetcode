class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        task = 0
        ans = 0
        for i in processorTime:
            core = 0
            count = 0
            while task < len(tasks) and core < 4:
                count = max(count, i + tasks[task])
                core+=1
                task+=1
            ans = max(ans, count)
        return ans