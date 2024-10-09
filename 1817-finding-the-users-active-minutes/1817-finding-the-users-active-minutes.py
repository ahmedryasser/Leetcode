from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        minutes = defaultdict(set)
        
        for id, value in logs:
            minutes[id].add(value)

        result = [0]*k
        for minute in minutes.values():
            result[len(minute)-1] +=1
        return result
        