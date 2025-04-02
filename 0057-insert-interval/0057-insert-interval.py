class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # for goes through each interval and checks if it contains a number bigger then or equal to newInterval[0]
        # if so add the beginning index to a var as start value
        # loop through the rest checks if it contains a number less then or equal to newInterval[1]
        # if so then add it as the end value
        
        result = []
        i = 0
        # Add all intervals ending before the new interval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # Merge all overlapping intervals to one considering newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval) # Add the merged interval
        # Add all the rest
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
