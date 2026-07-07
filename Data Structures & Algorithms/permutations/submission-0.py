class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            #base case
            if len(path) == len(nums):
                res.append(path[:])
                return

            #constraint: can't use the same number more than once
            for num in nums:
                if num in path: 
                    continue 
                
                path.append(num)
                backtrack(path) 
                path.pop()

        backtrack([])
        return res