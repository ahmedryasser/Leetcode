class Solution:
    def judgeCircle(self, moves: str) -> bool:
        xStack = []
        yStack = []
        for move in moves:
            if move == "L":
                if  xStack and xStack[-1] == "R":
                    xStack.pop()
                else:
                    xStack.append("L")
            elif move == "R":
                if xStack and xStack[-1] == "L":
                    xStack.pop()
                else:
                    xStack.append("R")
            elif move == "U":
                if yStack and yStack[-1] == "D":
                    yStack.pop()
                else:
                    yStack.append("U")
            elif move == "D":
                if yStack and yStack[-1] == "U":
                    yStack.pop()
                else:
                    yStack.append("D")
        return not xStack and not yStack