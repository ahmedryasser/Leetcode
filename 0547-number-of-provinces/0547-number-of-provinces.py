class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = defaultdict(list)
        n = len(isConnected)
        for node1 in range(n):
            for node2 in range(n):
                if isConnected[node1][node2] == 1 and node1 != node2:
                    adjList[node2].append(node1)
        print(adjList)
        visited = set()
        count = 0

        def bfs(i):
            stack = [i]
            while stack:
                node = stack.pop()
                visited.add(node)
                for nei in adjList[node]:
                    if nei not in visited:
                        stack.append(nei)
                 

        for i in range(n):
            if i not in visited:
                bfs(i)
                count+=1
        return count
        


