class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            slots-=1
            if slots<0:
                return False
            elif node != '#':
                slots+=2
        return slots == 0