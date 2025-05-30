class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        unique = {edge[0] for edge in edges}
        for _,val in edges:
            if val in unique:
                unique.remove(val)
        return list(unique)