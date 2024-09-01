class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        traversed = []
        direction = 0
        step = 1
        while len(traversed) < rows*cols:
            for _ in range(2):
                for i in range(step):
                    current = directions[direction]
                    if rStart>=0 and rStart<rows and cStart>=0 and cStart<cols:
                        traversed.append([rStart,cStart])
                    rStart+=current[0]
                    cStart+=current[1]
                direction = (direction+1)%4

            step+=1
        return traversed