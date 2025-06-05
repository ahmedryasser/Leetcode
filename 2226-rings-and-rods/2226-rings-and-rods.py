from collections import defaultdict
class Solution:
    def countPoints(self, rings: str) -> int:
        values = defaultdict(set)
        count = 0
        added = set()
        for i in range(0,len(rings), 2):
            values[rings[i+1]].add(rings[i])
            if len(values[rings[i+1]]) == 3 and rings[i+1] not in added:
                count+=1
                added.add(rings[i+1])
        return count