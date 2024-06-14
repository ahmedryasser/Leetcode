class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        largest = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] ==1:
                    neighbors=[(r,c)]
                    size = 1
                    while neighbors:
                        row,col = neighbors.pop(0) 
                        grid[row][col]=0
                        if col-1 >= 0 and grid[row][col-1] == 1:
                            if (row, col-1) not in neighbors: 
                                neighbors.append((row, col-1)) 
                                size+=1
                        if col+1 < len(grid[0]) and grid[row][col+1] == 1:
                            if (row, col+1) not in neighbors: 
                                neighbors.append((row, col+1))
                                size+=1
                        if row-1 >= 0 and grid[row-1][col] == 1:
                            if (row-1, col) not in neighbors: 
                                neighbors.append((row-1,col))
                                size+=1
                        if row+1 < len(grid) and grid[row+1][col] == 1: 
                            if (row+1, col) not in neighbors: 
                                neighbors.append((row+1,col))
                                size+=1
                    largest = max(size,largest)
                    size = 0
        return largest
            