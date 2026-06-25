class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers from opposite ends
        # return the max volume: max(height) * width 
        # move the lower height pointer to try to find the tallest one
        left,right = 0,len(heights) - 1
        res = 0

        while(right>left):
            min_height = min(heights[right],heights[left])
            area = min_height * (right-left)
            res = max(area,res)
            if heights[right] < heights[left]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1
        
        return res 

        