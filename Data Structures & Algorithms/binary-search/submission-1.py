import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # right and left pointer 
        # for each iteration we calculate mid = left + right // 2
        # we compare mid to the target, if it is return mid
        # if nums[mid] < target, we set left = mid
        # inverse if any different 
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1