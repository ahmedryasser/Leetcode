from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for preq in prerequisites:
            adj[preq[1]].append(preq[0])

        def dfs(num, stack, visited):
            if stack[num]:
                return True
            if visited[num]:
                return False
            stack[num] = True
            visited[num] = True

            for nei in adj[num]:
                if dfs(nei, stack, visited):
                    return True
            
            stack[num] = False
            return False
        stack = [False]*numCourses
        visited = [False]*numCourses
        for course in range(numCourses):
            if dfs(course, stack, visited):
                return False
        
        return True

