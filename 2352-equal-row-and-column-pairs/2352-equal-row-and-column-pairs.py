from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        columns =  defaultdict(list)
        
        for row in range(len(grid)):
            for col in range(len(grid)):
                columns[col].append(grid[row][col]) 
                
        cols = list(columns.values())
        
        for row in grid: 
            for col in cols:
                if col == row: result+=1
                    
        return result