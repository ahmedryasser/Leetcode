from collections import defaultdict, deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        gates = []
        for x,row in enumerate(rooms):
            for y,room in enumerate(row):
                if room == 0:
                    gates.append((x,y))
        queue = deque()            
        for gate in gates: queue.append((gate,0))

        def bfs():
            
            visited = set()
            
            while queue:
                crd,level = queue.popleft()
                x,y = crd
                rooms[x][y] = min(level, rooms[x][y])
                visited.add((x,y))
                for x2,y2 in directions:
                    if 0<= x+x2 <len(rooms) and 0<= y+y2 < len(rooms[0]) and rooms[x+x2][y+y2] != 0 and rooms[x+x2][y+y2] != -1 and (x+x2,y+y2) not in visited:
                        queue.append(((x+x2,y+y2), level+1))

        bfs()
        
        
        


        