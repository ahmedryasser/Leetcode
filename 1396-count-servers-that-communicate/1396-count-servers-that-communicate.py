from collections import defaultdict
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        comm = [0,0]
        visited = set()
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        def dfs(coord):
            visited.add(coord)
            x1,y1 = coord
            comm[1]+=1
            for x,y in rows[x1]:
                if len(grid)>x>=0 and 0<=y<len(grid[0]) and grid[x][y] == 1 and (x,y) not in visited:
                    dfs((x,y))
            for x,y in cols[y1]:
                if len(grid)>x>=0 and 0<=y<len(grid[0]) and grid[x][y] == 1 and (x,y) not in visited:
                    dfs((x,y))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i].add((i,j))
                    cols[j].add((i,j))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:

                    dfs((i,j))
                    if comm[1] >1: comm[0] += comm[1]
                    comm[1] = 0

        return comm[0]