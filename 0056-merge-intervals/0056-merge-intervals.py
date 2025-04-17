class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i,j = 0,1
        while j<len(intervals):
            if intervals[i][1] >= intervals[j][0]:
                intervals[i] = [min(intervals[i][0], intervals[j][0]), max(intervals[i][1], intervals[j][1]) ]
                intervals.pop(j)
            else:
                i=j
                j+=1
        return intervals