class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return None
        
        left,right = 0,1
        res = 0

        while(right < len(prices)):
            if prices[left] > prices[right]:
                left=right
                right += 1
            else:
                profit = prices[right]-prices[left]
                res = max(res,profit)
                right += 1
                
        return res
            
