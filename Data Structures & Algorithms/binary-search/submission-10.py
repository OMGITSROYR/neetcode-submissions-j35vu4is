class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while(right >= left):
            midpoint = (right + left) // 2
            print(midpoint)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint + 1
            
        return -1 
        