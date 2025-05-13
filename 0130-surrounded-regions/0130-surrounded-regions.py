class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # start with all 4 sides, if theres a O then bfs and add all values to a list.
        # Set every other unmarked O to X
        stack = []
        visited = set()
        directions  = [(0,1), (1,0), (0,-1), (-1, 0)]
        for x,row in enumerate(board):
            for y,val in enumerate(row):
                if (x == 0 or x == len(board)-1 or y == 0 or y == len(row)-1) and val == "O":
                    stack.append((x,y))

        while stack:
            x1,y1 = stack.pop()
            board_length = len(board)
            visited.add((x1,y1))
            for x2,y2 in directions:
                if 0<= x1+x2 <board_length and 0<= y1+y2 <len(board[0]) and board[x1+x2][y1+y2] == "O" and (x1+x2,y1+y2) not in visited:
                    stack.append((x1+x2,y1+y2))

        for x,row in enumerate(board):
            for y,val in enumerate(row):
                if (x,y) not in visited and val == "O":
                    board[x][y] = "X"
            
        



                

