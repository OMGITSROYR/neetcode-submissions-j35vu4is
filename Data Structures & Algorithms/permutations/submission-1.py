class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False] * len(nums)
        
        def dfs(curr, picked):
            if len(nums) == len(curr):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    dfs(curr, picked)                  
                    curr.pop()
                    picked[i] = False

        dfs([],picked)
        return res