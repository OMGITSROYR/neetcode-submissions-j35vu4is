class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        prev = None
        streak = 0

        for num in nums:
            if num == 1:
                streak += 1
            else:
                res = max(res,streak)
                streak = 0

        res = max(res,streak)
        return res