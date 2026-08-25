class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        count = 0
        heapq.heapify(heap)

        for xi,yi in points:
            dist = ( (xi**2) + (yi**2) ) ** (1/2)
            heapq.heappush( heap, (dist,count,[xi,yi]) )
            count += 1

        for i in range(k):
            dist,count,point = heapq.heappop(heap)
            res.append(point)

        return res