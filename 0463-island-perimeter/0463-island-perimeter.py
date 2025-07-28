class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = [0]
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        visited = set()
        def dfs(node):
            x1,y1 = node
            visited.add(node)
            running = 0
            for x2,y2 in directions:
                x,y = x1+x2, y1+y2
                if (x,y) not in visited and len(grid)>x>=0 and len(grid[0])>y>=0 and grid[x][y] == 1:
                    dfs((x,y))
                elif (x,y) not in visited:
                    running+=1
            count[0] += running

            return running
        flag = 0
        res = -1
        for i,row in enumerate(grid):
            if flag == 1:
                break
            for j,item in enumerate(row):
                if item == 1:
                    res = dfs((i,j))
                    flag = 1
                    break
        return count[0]
            




