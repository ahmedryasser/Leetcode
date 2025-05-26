class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vals = set()
        for edge in edges:
            if edge[0] in vals:
                return edge[0]
            elif edge[1] in vals:
                return edge[1]
            else:
                vals.add(edge[0])
                vals.add(edge[1])