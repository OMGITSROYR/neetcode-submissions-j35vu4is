class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # have a min heap 
        # push everything by enqueue, keep count, and push everything once the count > enquetime processing time
        # return top of min
        res = []
        time = 1
        pending = []
        available = []
        heapq.heapify(pending)
        heapq.heapify(available)

        for i,p in enumerate(tasks):
            enqueueTime,processingTime = p
            heapq.heappush(pending,(enqueueTime,processingTime,i))

        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueTime,processingTime,i = heapq.heappop(pending)
                heapq.heappush(available, (processingTime,i))
            
            if not available:
                time = pending[0][0]
                continue

            processingTime,i = heapq.heappop(available)
            res.append(i)
            time += processingTime
        
        return res









