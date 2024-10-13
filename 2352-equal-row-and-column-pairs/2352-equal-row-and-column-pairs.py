class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        columns = {}
        
        for row in range(len(grid)):
            for col in range(len(grid)):
                val = columns.get(col,[])
                val.append(grid[row][col])
                columns[col] = val
        print(columns)
        cols = list(columns.values())
        for row in grid: 
            for col in cols:
                if col == row: result+=1
        return result