class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0,0)
        mapping = {"N": (1,0), "S": (-1,0), "E": (0,1), "W": (0,-1)}
        path_arr = [(0,0)]
        path_set = {(0,0)}
        for c in path:
            x,y = current
            x += mapping[c][0]
            y += mapping[c][1]

            current = (x,y)
            path_set.add(current)
            path_arr.append(current)
        
        return len(path_set) != len(path_arr)
            