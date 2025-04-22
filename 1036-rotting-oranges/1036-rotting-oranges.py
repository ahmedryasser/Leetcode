from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROW,COL = len(grid),len(grid[0])
        fresh_oranges = 0
        minutes_elapsed = -1
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh_oranges+=1
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue.append((-1,-1))
        while queue:
            row,col = queue.popleft()
            if row == -1:
                minutes_elapsed+=1
                if queue:
                    queue.append((-1,-1))
            else:
                for direction in directions:
                    x,y = row+direction[0], col+direction[1]
                    if 0 <= x <ROW and 0 <= y < COL:
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            fresh_oranges -=1
                            queue.append((x,y))

        return minutes_elapsed if fresh_oranges == 0 else -1
                

        

