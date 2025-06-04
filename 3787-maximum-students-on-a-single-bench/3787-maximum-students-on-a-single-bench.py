from collections import defaultdict
class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        values = defaultdict(set)
        for student,bench in students:
            values[bench].add(student)
        
        highest = 0
        for count in values.values():
            highest = max(highest,len(count))
        return highest