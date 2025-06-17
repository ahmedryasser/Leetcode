class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right = max(piles)
        def evaluate(k):
            count = 0
            for pile in piles:
                count += pile//k
                count += 0 if pile%k == 0 else 1
                if count >h:
                    return False
            return True

        final = 0
        while left <= right:
            mid = (left+right)//2
            result = evaluate(mid)
            if result:
                final = mid
                right = mid - 1
            else:
                left = mid + 1
        return final