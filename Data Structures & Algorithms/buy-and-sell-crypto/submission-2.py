class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        max_profit = 0

        while right <= len(prices) - 1:
            if prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                max_profit = max(diff,max_profit)
                right += 1
            else:
                left = right
                right += 1
        return max_profit