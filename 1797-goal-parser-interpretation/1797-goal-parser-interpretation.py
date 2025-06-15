class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        result = []
        i=0
        while i < len(command):
            if command[i] == "G":
                result.append("G")
                i+=1
            else:
                j=i
                while command[j] != ")":
                    j+=1
                if j-i == 1:
                    result.append("o")
                else:
                    result.append("al")
                i=j+1
        return "".join(result)

