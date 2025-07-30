class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0
        visited = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(coord):
            stack = [coord]
            visited.add(coord)
            while stack:
                node = stack.pop()
                x,y = node
                visited.add(node)
                for direction in directions:
                    new_x = x+direction[0]
                    new_y = y+direction[1]
                    if new_x>=0 and new_x<len(grid) and new_y>= 0 and new_y<len(grid[0]) and grid[new_x][new_y] == "1" and (new_x,new_y) not in visited:
                        stack.append((new_x,new_y))
                        visited.add((new_x,new_y))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                val = (x,y)
                if val not in visited and grid[x][y] == "1":
                    number+=1
                    dfs((x,y))
        return number