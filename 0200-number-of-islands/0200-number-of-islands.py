class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = 0 # grid is now visited
                    neighbors = []
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.pop(0)
                        if row - 1 >= 0 and grid[row - 1][col] == "1": # left
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"
                        if row + 1 < rows and grid[row + 1][col] == "1": # right
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = "0"
                        if col - 1 >= 0 and grid[row][col - 1] == "1": #above
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = "0"
                        if col + 1 < cols and grid[row][col + 1] == "1": #below
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"
        return num_islands