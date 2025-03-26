class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(rest):
            if rest < 0:
                return -1
            if rest == 0:
                return 0
            min_val = float('inf')
            for coin in coins:
                val = dfs(rest - coin)
                if val != -1:
                    min_val = min(min_val, val+1)
            return min_val if min_val != float('inf') else -1
        return dfs(amount)
