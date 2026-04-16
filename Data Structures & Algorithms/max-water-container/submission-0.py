class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left,right = 0,len(heights) - 1

        while right > left:
            curr_area = (right - left) * min(heights[left],heights[right])
            max_area = max(curr_area,max_area)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
                left += 1

        return max_area