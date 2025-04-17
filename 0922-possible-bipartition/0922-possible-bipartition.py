from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for entry in dislikes:
            adjList[entry[0]].add(entry[1])
            adjList[entry[1]].add(entry[0])
        colors = {}
        def dfs(person, color):
            if person in colors:
                return colors[person] == color
            colors[person] = color
            return all(dfs(neighbor, color^1) for neighbor in adjList[person])
        
        return all(dfs(node,0) for node in adjList.keys() if node not in colors)
