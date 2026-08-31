class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        curr = 0

        for num in nums:
            if num == 1:
                if curr == 1:
                    streak += 1
                else:
                    streak = 1
            else:
                streak = 0
                
            curr = num
            res = max(res,streak)

        return res

