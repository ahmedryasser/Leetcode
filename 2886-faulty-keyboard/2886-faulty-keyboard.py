class Solution:
    def finalString(self, s: str) -> str:
        vals= []
        result = []
        latest = 0
        for i,c in enumerate(s):
            if c == 'i':
                vals = vals[::-1]
            else:
                vals.append(c)

        return "".join(vals)
            