class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        res = right

        while(right >= left):
            k = (right + left) // 2

            counter = 0
            for p in piles:
                counter += math.ceil(float(p) / k)
            if counter <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res