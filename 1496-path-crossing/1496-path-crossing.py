class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0,0)
        mapping = {"N": (1,0), "S": (-1,0), "E": (0,1), "W": (0,-1)}
        path_set = {(0,0)}
        for c in path:
            x,y = current
            x += mapping[c][0]
            y += mapping[c][1]
            current = (x,y)
            if current in path_set:
                return True
            path_set.add(current)
            
        return False
        
        return False
            