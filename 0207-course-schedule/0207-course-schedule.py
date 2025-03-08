from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for preq in prerequisites:
            adj[preq[1]].append(preq[0])

        def dfs(num, stack, visted):
            if stack[num]:
                return True
            if visted[num]:
                return False
            stack[num] = True
            visited[num] = True
            for i in adj[num]:
                if dfs(i,stack,visited):
                    return True
            stack[num] = False
            return False

        stack = [False]*numCourses
        visited = [False]*numCourses
        for num in range(numCourses):
            if dfs(num,stack,visited):
                return False
        return True

        
        return True