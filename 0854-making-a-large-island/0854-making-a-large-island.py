class Solution:
    def largestIsland(self, matrix: List[List[int]]) -> int:
        visited = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        tot = []
        curr = 2
        def dfs(coord):
            visited.add(coord)
            tot[curr-2]+=1
            x1,y1 = coord
            matrix[x1][y1] = curr
            for x2,y2 in directions:
                x,y = x1+x2,y1+y2
                if len(matrix)>x>=0 and 0<=y<len(matrix[0]) and matrix[x][y] == 1 and (x,y) not in visited:
                    dfs((x,y)) 
        sizes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    tot.append(0)
                    dfs((i,j))
                    sizes.append(tot[0])
                    curr+=1
        biggest = max(tot+[0])        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    res = 1
                    counted = set()
                    for x,y in directions:
                        if len(matrix)>x+i>=0 and 0<=y+j<len(matrix[0]) and matrix[x+i][y+j] > 1 and matrix[x+i][y+j]-2 not in counted: 
                            count = matrix[x+i][y+j]-2
                            res+= tot[count]
                            counted.add(count)
                    biggest = max(biggest,res)
        return biggest