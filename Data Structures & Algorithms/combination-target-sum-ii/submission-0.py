class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def dfs(i):
            local = 0
            for num in cur:
                local += num
            if local > target:
                return
            if local == target:
                res.append(cur.copy())
                return
            if i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i+1)
            cur.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res