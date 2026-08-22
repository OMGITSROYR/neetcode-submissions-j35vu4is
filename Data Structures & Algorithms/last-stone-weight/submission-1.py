class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = []
        heapq.heapify(weights)
        for stone in stones:
            heapq.heappush(weights,-stone)

        while(len(weights) > 0):
            if len(weights) > 1:
                one = -heapq.heappop(weights)
                two = -heapq.heappop(weights)
                if one < two:
                    heapq.heappush(weights,-(two-one))
                elif one > two:
                    heapq.heappush(weights,-(one-two))
            elif len(weights) == 1:
                return - heapq.heappop(weights)
        
        return 0