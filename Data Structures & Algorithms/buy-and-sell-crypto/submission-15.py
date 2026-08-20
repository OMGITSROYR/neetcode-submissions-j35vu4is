class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the greatest difference between 2 values
        res = 0
        left = 0
        right = 1

        if len(prices) == 2:
            if prices[1]-prices[0] > 0:
                return prices[1]-prices[0]
            return res

        while(right <= (len(prices) - 1)):

            if prices[right] < prices[left]:
                left = right
                if right == len(prices) - 2:
                    right += 1
                continue

            res = max(res,prices[right] - prices[left])
            print(res)
            right += 1

        return res

