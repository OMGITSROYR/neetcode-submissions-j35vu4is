class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while(left<right):
                threeSum = nums[i] + nums[right] + nums[left]
                if threeSum == 0:
                    res.append([nums[i],nums[right],nums[left]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                
        return res
            


        