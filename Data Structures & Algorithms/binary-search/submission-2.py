import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # right and left pointer 
        # for each iteration we calculate mid = left + right // 2
        # we compare mid to the target, if it is return mid
        # if nums[mid] < target, we set left = mid
        # inverse if any different 
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1