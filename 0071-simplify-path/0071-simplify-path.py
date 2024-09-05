class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for direc in paths:
            if direc == ".." and stack:
                stack.pop()
            elif direc == "." or direc == "" or direc == "..":
                continue
            else:
                stack.append(direc)
        return "/" +"/".join(stack)
            