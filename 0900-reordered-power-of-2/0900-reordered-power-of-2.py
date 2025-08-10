class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        for i in range(30):
            val = Counter(str(2**i))
            if val == count:
                return True
        return False

