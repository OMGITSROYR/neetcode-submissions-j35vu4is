class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row):
            for j in range(col):
                print(res)
                found = False

                if grid[i][j] == 0:
                    continue

                # but if it is 1, we have to check how many servers can communicate
                for k in range(row):
                    if k == i:
                        continue
                    if grid[k][j] == 1:
                        found=True
                        break

                if not found:
                    for g in range(col):
                        if j == g:
                            continue
                        if grid[i][g] == 1:
                            found=True
                            break
                if found:
                    res += 1

        return res
            