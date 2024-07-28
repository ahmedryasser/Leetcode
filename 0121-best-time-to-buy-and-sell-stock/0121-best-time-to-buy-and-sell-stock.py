class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit =0
        # for indexA in range(len(prices)):
        #     localProfit = 0
        #     for indexB in range(indexA+1, len(prices)):   
        #         currProfit = prices[indexB] - prices[indexA]
        #         if currProfit>localProfit:
        #             localProfit = currProfit
        #     if localProfit>profit:
        #         profit = localProfit
        # return profit
        
        # start = min(prices)
        # for i,price in enumerate(prices):
        #     if price == start:
        #         return max(prices[i:]) - start
        
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit